import sqlite3
from pathlib import Path

from src.config import DATABASE_PATH
from src.logger import get_logger

logger = get_logger(__name__)

TABLE_NAME = "books"


def save_to_database(df):
    if df is None or df.empty:
        logger.warning("No data to save. The DataFrame is empty.")
        return False

    connection = None

    try:
        db_file = Path(DATABASE_PATH)

        db_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        logger.info(
            f"Connecting to database: {db_file}"
        )

        connection = sqlite3.connect(db_file)

        df.to_sql(
            TABLE_NAME,
            connection,
            if_exists="replace",
            index=False
        )

        logger.info(
            f"Saved {len(df)} rows to the '{TABLE_NAME}' table."
        )

        return True

    except sqlite3.Error as error:
        logger.error(
            f"Database error: {error}"
        )
        return False

    except Exception as error:
        logger.error(
            f"Unexpected error while saving to database: {error}"
        )
        return False

    finally:
        if connection is not None:
            connection.close()
            logger.info(
                "Database connection closed."
            )