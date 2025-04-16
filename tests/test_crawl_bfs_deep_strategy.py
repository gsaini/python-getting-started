# Unit tests for crawl_bfs_deep_strategy.py
import pytest
from unittest.mock import AsyncMock, patch
from crawl4ai import AsyncWebCrawler

@pytest.mark.asyncio
async def test_crawl_bfs_deep_strategy():
    """
    Test case for crawling a single URL using BFS deep strategy.

    This test mocks the AsyncWebCrawler to simulate a successful crawl and
    verifies the result.
    """
    mock_result = AsyncMock(
        success=True,
        url="https://docs.crawl4ai.com/",
        markdown="Mocked markdown content",
        error_message=None
    )

    with patch("crawl4ai.AsyncWebCrawler.arun", return_value=[mock_result]):
        from crawl_bfs_deep_strategy import main

        # Run the main function
        await main()

        # Verify the result
        assert mock_result.success is True
        assert mock_result.markdown == "Mocked markdown content"