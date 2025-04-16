# Optimized the code and added detailed function comments
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

async def main():
    """
    Main function to crawl a single page using LLM extraction strategy.

    This function defines the LLM extraction strategy, sets up the crawler
    configuration, and processes the result of crawling a single page. It
    prints the status code, response headers, and markdown content if the
    crawl is successful. Errors are logged otherwise.

    Returns:
        None
    """
    # Define the LLM extraction strategy
    llm_strategy = LLMExtractionStrategy(
        llm_config=LLMConfig(provider="ollama/tinyllama"),
        extraction_type="block",
        instruction="Please ensure to extract all the information which is accurate and relevant to Crawl4AI.",
        chunk_token_threshold=1000,
        overlap_rate=0.0,
        apply_chunking=True,
        input_format="markdown",
    )

    # Build the crawler configuration
    crawl_config = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASS,
        check_robots_txt=True,
        exclude_external_links=True,
        exclude_social_media_links=True,
        exclude_domains=["ads.example.com"],
        exclude_social_media_domains=["facebook.com", "twitter.com", "instagram.com"],
        exclude_external_images=True,
        delay_before_return_html=2.0,
        page_timeout=60000,
    )

    # Create a browser configuration
    browser_cfg = BrowserConfig(headless=True)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # Crawl a single page
        result = await crawler.arun(
            url="https://docs.crawl4ai.com/",
            config=crawl_config
        )

        if result.success:
            print(result.status_code, result.response_headers)

            if result.markdown:
                print("Markdown snippet:", result.markdown.raw_markdown)
                # Save the entire markdown to a file
                with open('page_content.md', 'w', encoding='utf-8') as md_file:
                    md_file.write(result.markdown)

                # Show usage stats
                llm_strategy.show_usage()  # prints token usage
        else:
            print("Error:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())