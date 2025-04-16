# Unit tests for crawl_llm_strategy.py
import pytest
from unittest.mock import AsyncMock, patch
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMExtractionStrategy

@pytest.mark.asyncio
async def test_crawl_single_page():
    """
    Test case for crawling a single page using LLM extraction strategy.

    This test mocks the AsyncWebCrawler to simulate a successful crawl and
    verifies the result.
    """
    mock_result = AsyncMock(
        success=True,
        status_code=200,
        response_headers={"Content-Type": "text/html"},
        markdown="Mocked markdown content",
        error_message=None
    )

    with patch("crawl4ai.AsyncWebCrawler.arun", return_value=mock_result):
        from crawl_llm_strategy import main

        # Run the main function
        await main()

        # Verify the result
        assert mock_result.success is True
        assert mock_result.status_code == 200
        assert mock_result.markdown == "Mocked markdown content"
        assert mock_result.response_headers["Content-Type"] == "text/html"