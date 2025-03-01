import json
import os

from dotenv import load_dotenv

from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()


graph_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}


smart_scraper_graph = SmartScraperGraph(
    prompt="Give me all the news",
    source="https://www.wired.com/",
    config=graph_config,
)

result = smart_scraper_graph.run()
print(json.dumps(result, indent=4))

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))
