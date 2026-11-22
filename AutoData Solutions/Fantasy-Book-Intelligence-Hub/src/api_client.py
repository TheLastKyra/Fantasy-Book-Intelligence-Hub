import requests

from src.config import API_BASE_URL, REQUEST_TIMEOUT
from src.logger import get_logger

logger = get_logger(__name__)


def search_books(search_term, max_results=5):
    """Search Open Library and return JSON data."""

    parameters = {
        "q": search_term,
        "limit": max_results,
    }

    logger.info(f"Searching Open Library for '{search_term}'")

    try:
        response = requests.get(
            API_BASE_URL,
            params=parameters,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        data = response.json()

        logger.info(
            f"Success. Open Library returned {data.get('numFound', 0)} matches."
        )

        return data

    except requests.exceptions.RequestException as error:
        logger.error(f"API request failed: {error}")
        return None


if __name__ == "__main__":
    result = search_books("Red Rising")

    if result:
        print(f"Total items found: {result.get('numFound', 0)}")
        print(f"Results returned: {len(result.get('docs', []))}")
    else:
        print("Search failed.")