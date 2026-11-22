import logging
import os

from src.config import LOG_FILE_PATH


def get_logger(name="fantasy_book_hub"):
    """
    Create (or fetch) a logger that writes to both
    the terminal and the log file.
    """

    log_folder = os.path.dirname(str(LOG_FILE_PATH))

    if log_folder:
        os.makedirs(log_folder, exist_ok=True)

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    log_format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    formatter = logging.Formatter(
        log_format,
        datefmt=date_format
    )

    file_handler = logging.FileHandler(
        LOG_FILE_PATH,
        mode="a",
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger


if __name__ == "__main__":
    test_logger = get_logger("logger_test")

    test_logger.info(
        "Logger is working - this is an INFO message."
    )

    test_logger.warning(
        "This is a WARNING message."
    )

    test_logger.error(
        "This is an ERROR message."
    )

    print(
        f"\nCheck your log file here: {LOG_FILE_PATH}"
    )