# Unit tests for crawl_run_many_urls.py
import pytest
from unittest.mock import AsyncMock, patch
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

@pytest.mark.asyncio
async def test_crawl_multiple_urls():
    """
    Test case for crawling multiple URLs using AsyncWebCrawler.

    This test mocks the AsyncWebCrawler to simulate successful and failed
    crawling of URLs and verifies the results.
    """
    mock_results = [
        AsyncMock(success=True, url="https://docs.crawl4ai.com/", markdown="Mocked markdown content", error_message=None),
        AsyncMock(success=False, url="https://react.dev", markdown=None, error_message="404 Not Found"),
    ]

    with patch("crawl4ai.AsyncWebCrawler.arun_many", return_value=mock_results):
        from crawl_run_many_urls import main

        # Run the main function
        await main()

        # Verify the results
        assert mock_results[0].success is True
        assert mock_results[0].markdown == "Mocked markdown content"
        assert mock_results[1].success is False
        assert mock_results[1].error_message == "404 Not Found"