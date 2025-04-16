import os
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, LLMConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.extraction_strategy import LLMExtractionStrategy

import re  # Add re module for sanitizing URLs

# Define the LLM extraction strategy
llm_strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(provider="ollama/tinyllama"),
    # schema=Product.model_json_schema(), # Or use model_json_schema()
    extraction_type="block",
    instruction="Please ensure to extract the information which is accurate and relevant to ",
    chunk_token_threshold=1000,
    overlap_rate=0.0,
    apply_chunking=True,
    input_format="markdown",  # or "html", "fit_markdown"
    # extra_args={"temperature": 0.0, "max_tokens": 800}
)

config = CrawlerRunConfig(
    # The BFSDeepCrawlStrategy uses a breadth-first approach, exploring all links at one depth before moving deeper.
    deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=2, include_external=False),
    # extraction_strategy=llm_strategy,
    stream=False,  # Default behavior,
    check_robots_txt=True,  # Respect robots.txt rules
    exclude_external_links=True,  # Remove external links from final content
    exclude_social_media_links=True,  # Remove links to known social sites
    exclude_domains=[""],  # Exclude links to these domains
    exclude_social_media_domains=[
        "facebook.com",
        "twitter.com",
        "instagram.com",
    ],  # Extend the default list
    exclude_external_images=True,  # Strip images from other domains
    #delay_before_return_html=2.0,  # Wait 2s before capturing final HTML
    semaphore_count=3,  # Limit the number of concurrent requests
)

async def main():
    # Create a browser config if needed
    browser_cfg = BrowserConfig(headless=True)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # Wait for ALL results to be collected before returning
        results = await crawler.arun('https://docs.crawl4ai.com/', config=config)

        for result in results:
            if result.success:
                # Check if the result contains the extracted content
                if result.markdown:
                    # Save the entire markdown to a file
                    folder_name = "bfs_content_single"
                    os.makedirs(folder_name, exist_ok=True)  # Ensure the folder exists
                    url_path = sanitize_url(result.url)

                    # Ensure sanitize_url is defined
                    filename = os.path.join(folder_name, f"{url_path}.md")
                    with open(filename, "w", encoding="utf-8") as md_file:
                        md_file.write(result.markdown)

                    print(f"Successfully crawled {result.url}")

                else:
                    print("Error:", result.error_message)

            elif result.status_code == 403 and "robots.txt" in result.error_message:
                print(f"Skipped {result.url} - blocked by robots.txt")

            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")

# Utility function to sanitize URLs
def sanitize_url(url: str) -> str:
    # Replace invalid filename characters with underscores
    return re.sub(r'[<>:"/\\|?*]', "_", url)

# Run the async function
asyncio.run(main())
