from src.extract import extract_books
from src.clean import clean_books
from src.database import save_to_database
from src.logger import get_logger

logger = get_logger(__name__)


def run_pipeline():
    logger.info("=== Pipeline started ===")

    try:
        logger.info("Step 1/3: Extracting book data...")
        raw_data = extract_books()

        if not raw_data:
            logger.error("No data was extracted. Stopping the pipeline.")
            return False

        logger.info("Extraction finished.")

        logger.info("Step 2/3: Cleaning book data...")
        df = clean_books(raw_data)

        if df is None or df.empty:
            logger.error("Cleaning produced no data. Stopping the pipeline.")
            return False

        logger.info(
            f"Cleaning finished. Rows ready to save: {len(df)}"
        )

        logger.info("Step 3/3: Saving data to the database...")
        save_to_database(df)

        logger.info("Saving finished.")

    except Exception as error:
        logger.exception(
            f"Pipeline failed with an error: {error}"
        )
        return False

    logger.info("=== Pipeline completed successfully ===")

    return True


if __name__ == "__main__":
    success = run_pipeline()

    raise SystemExit(0 if success else 1)