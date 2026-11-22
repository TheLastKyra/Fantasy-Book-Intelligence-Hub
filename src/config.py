from pathlib import Path

# ---------------------------------------------------------------
# 1. PROJECT FOLDERS
# ---------------------------------------------------------------
# __file__ is the location of this config.py file.
# .resolve().parent gives us the folder that contains it.
# Using this means the project works no matter where it is stored
# on your computer (important for Windows Task Scheduler later).
BASE_DIR = Path(__file__).resolve().parent.parent

# Folders where we will keep our database and log files.
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# Create the folders if they don't exist yet.
# exist_ok=True means "don't complain if it's already there".
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------
# 2. GOOGLE BOOKS API
# ---------------------------------------------------------------
# The address we send our book searches to.
API_BASE_URL = "https://openlibrary.org/search.json"

# Google allows a maximum of 40 books per request.
MAX_RESULTS_PER_REQUEST = 40

# How many seconds to wait for Google to reply before giving up.
REQUEST_TIMEOUT = 10

# ---------------------------------------------------------------
# 3. SQLITE DATABASE
# ---------------------------------------------------------------
# SQLite stores everything in a single file.
# This will create/use:  <project folder>/data/fantasy_books.db
DATABASE_PATH = DATA_DIR / "fantasy_books.db"

# ---------------------------------------------------------------
# 4. LOGGING
# ---------------------------------------------------------------
# The log file records what the pipeline did and any errors.
# This will create/use:  <project folder>/logs/pipeline.log
LOG_FILE_PATH = LOG_DIR / "pipeline.log"

# ---------------------------------------------------------------
# 5. FANTASY SEARCH TERMS
# ---------------------------------------------------------------
# Each term is sent to the API as its own search.
# "subject:" tells Google to search by book category.
# You can add or remove terms freely.
SEARCH_TERMS = [
    "Red Rising",
    "The Poppy War",
    "The Stormlight Archive",
    "Throne of Glass",
    "Dune",
    "The Bloodsworn Saga"
]