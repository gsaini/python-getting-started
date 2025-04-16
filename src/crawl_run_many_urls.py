# Optimized the code and added detailed function comments
import asyncio
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

# List of URLs to crawl
urls_to_crawl = [
    "https://docs.crawl4ai.com/",
    "https://react.dev",
]

# Configuration for the crawler
config = CrawlerRunConfig(
    stream=False,  # Default behavior
    check_robots_txt=True,  # Respect robots.txt rules
    exclude_external_links=True,  # Remove external links from final content
    exclude_social_media_links=True,  # Remove links to known social sites
    exclude_domains=[],  # Exclude links to these domains
    exclude_social_media_domains=[
        "facebook.com",
        "twitter.com",
        "instagram.com",
    ],  # Extend the default list
    exclude_external_images=True,  # Strip images from other domains
    semaphore_count=3,  # Limit the number of concurrent requests
)

async def main():
    """
    Main function to crawl multiple URLs using AsyncWebCrawler.

    This function initializes the browser configuration, sets up the crawler,
    and processes the results of crawling multiple URLs. It prints the status
    of each URL (success or failure) and logs any errors encountered.

    Returns:
        None
    """
    # Create a browser configuration
    browser_cfg = BrowserConfig(headless=True)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # Crawl multiple URLs and collect results
        results = await crawler.arun_many(
            urls=urls_to_crawl,
            config=config,
        )

        # Process and print the results
        for result in results:
            if result.success:
                print(f"{result.url} crawled OK!")
            else:
                print(f"Failed: {result.url} - {result.error_message}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
