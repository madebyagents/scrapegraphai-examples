# ScrapeGraphAI Demo

This repository contains examples of using the [ScrapeGraphAI](https://scrapegraphai.com/?via=tobias) platform for web scraping with AI-powered capabilities.

## Overview

ScrapeGraphAI is a powerful platform that combines web scraping with AI processing to extract meaningful data from websites. This demo shows two approaches:

1. **Using the Python Library** - Direct integration with the `scrapegraphai` library
2. **Using the API** - Interaction through the `scrapegraph_py` client

## Examples

### Library Example (`scraping_library.py`)

This example demonstrates using the ScrapeGraphAI library directly to scrape news from Wired.com:

```python
from scrapegraphai.graphs import SmartScraperGraph

smart_scraper_graph = SmartScraperGraph(
    prompt="Give me all the news",
    source="https://www.wired.com/",
    config=graph_config,
)

result = smart_scraper_graph.run()
```

### API Example (`scraping_api.py`)

This example shows how to use the ScrapeGraphAI API client to extract product information from Amazon:

```python
from scrapegraph_py import Client

sgai_client = Client()
response = sgai_client.smartscraper(
    website_url="https://www.amazon.it/s?k=keyboard",
    user_prompt="Extract the names and prices of all keyboards",
)
```

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your API keys
6. Run an example: `python scraping_library.py` or `python scraping_api.py`

## Requirements

- Python 3.8+
- ScrapeGraphAI API key
- OpenAI API key (for certain models)

## License

MIT 
