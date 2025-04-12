import asyncio
import json
import re # For potentially cleaning up LLM output
import os # To check if file exists for appending (optional logic)
from crawl4ai import AsyncWebCrawler

# --- Configuration ---

# URL of the site/page you want to crawl
target_url = 'https://react.dev/' # Example: LangChain blog

# Ollama LLM Configuration
ollama_llm_config = {
    "provider": "ollama",
    "model": "llama3:instruct", # IMPORTANT: Change if needed
    "base_url": "http://localhost:11434/api",
}

# Extraction Prompt (same as before)
extraction_prompt = """
Extract the most important information about the React library from https://react.dev. Focus on:
1.  What React is and its main goal.
2.  The core concepts or building blocks (like Components, State, Props, JSX, Hooks).
3.  The major benefits of using React.
4.  How to typically start a new project.

Please summarize these points clearly. You can use a JSON object with keys like "summary", "core_concepts", "benefits", "getting_started", or present it as well-structured markdown text.
"""
# extraction_prompt = """
# Based on the provided web page content, extract the following information for the main article(s) present:
# 1.  The main title of the article.
# 2.  A brief summary of the article (1-2 sentences).
# 3.  The author's name, if available.
# 4.  The publication date, if available.

# Please provide the extracted information in JSON format. If multiple articles are clearly distinct on the page, provide a JSON array, otherwise provide a single JSON object. Example format:
# {
#   "title": "...",
#   "summary": "...",
#   "author": "...",
#   "publicationDate": "..."
# }
# or
# [
#   { "title": "...", "summary": "...", ... },
#   { "title": "...", "summary": "...", ... }
# ]
# If information is not found, use null or omit the key. Focus on the primary content. Do not include ```json markers in your output.


# --- File to save extracted data ---
output_filename = "extracted_content-01.json"

# --- Main Crawling Logic ---

async def main():
    print(f"Starting crawl for: {target_url}")
    print(f"Using Ollama model: {ollama_llm_config['model']}")

    all_extracted_data = [] # List to hold data from multiple pages if max_pages > 1

    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(
                url=target_url,
                llm_config=ollama_llm_config,
                extraction_prompt=extraction_prompt,
                crawler_options={
                    "max_pages": 1, # Set to > 1 to crawl multiple pages
                    "max_depth": 0,
                }
            )

        print('\n--- Crawl Result ---', result.markdown)
        # Save the entire markdown to a file
        with open('page_content.md', 'w', encoding='utf-8') as md_file:
            md_file.write(result.markdown)


    except Exception as e:
        print(f'\nAn error occurred during the crawling process: {e}')
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
