import pandas as pd

from src.logger import get_logger

logger = get_logger(__name__)


def clean_books(raw_books):
    """
    Convert raw Open Library data into
    a clean pandas DataFrame.
    """

    cleaned_books = []

    for book in raw_books:
        title = book.get("title", "Unknown")

        # Standardize apostrophes
        title = title.replace("’", "'")

        cleaned_books.append(
            {
                "title": title,
                "author": ", ".join(
                    book.get("author_name", ["Unknown"])
                ),
                "publish_year": book.get(
                    "first_publish_year"
                ),
                "language": ", ".join(
                    book.get("language", ["Unknown"])
                ),
            }
        )

    df = pd.DataFrame(cleaned_books)

    # Remove omnibus editions
    df = df[
        ~df["title"].str.contains(
            "/",
            na=False
        )
    ]

    # Remove unrelated title
    df = df[
        df["title"] != "Where Poppies Grow"
    ]

    # Remove translated/duplicate edition
    df = df[
        df["title"] != "THE POPPY WAR"
    ]

    # Remove duplicate titles
    df = df.drop_duplicates(
        subset=["title"]
    )

    df = df.fillna("Unknown")

    logger.info(
        f"Cleaning complete. Records remaining: {len(df)}"
    )

    return df