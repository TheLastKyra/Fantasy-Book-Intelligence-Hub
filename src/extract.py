from src.api_client import search_books
from src.config import SEARCH_TERMS
from src.logger import get_logger

logger = get_logger(__name__)


def extract_books():
    """
    Retrieve book data for all search terms.
    """

    all_books = []

    for term in SEARCH_TERMS:
        logger.info(f"Starting search for: {term}")

        result = search_books(term, max_results=5)

        if result and "docs" in result:
            books = result["docs"]

            logger.info(
                f"Retrieved {len(books)} books for '{term}'"
            )

            all_books.extend(books)

        else:
            logger.warning(
                f"No data returned for '{term}'"
            )

    logger.info(
        f"Extraction complete. Total books collected: {len(all_books)}"
    )

    return all_books


if __name__ == "__main__":
    books = extract_books()

    print(f"\nTotal books collected: {len(books)}")