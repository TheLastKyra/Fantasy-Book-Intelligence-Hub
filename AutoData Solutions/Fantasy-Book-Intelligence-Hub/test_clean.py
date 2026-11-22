from src.extract import extract_books
from src.clean import clean_books

books = extract_books()

df = clean_books(books)

print(df)