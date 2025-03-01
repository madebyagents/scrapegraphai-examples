from scrapegraph_py import Client
from scrapegraph_py.logger import sgai_logger

sgai_logger.set_logging(level="INFO")

sgai_client = Client()


response = sgai_client.smartscraper(
    website_url="https://www.amazon.it/s?k=keyboard",
    user_prompt="Extract the names and prices of all keyboards",
)

print(f"Request ID: {response['request_id']}")
print(f"Result: {response['result']}")

sgai_client.close()
