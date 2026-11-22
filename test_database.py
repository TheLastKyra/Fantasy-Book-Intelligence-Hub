from src.extract import extract_books
from src.clean import clean_books
from src.database import save_to_database

books = extract_books()

df = clean_books(books)

save_to_database(df)

print("Database saved successfully.")