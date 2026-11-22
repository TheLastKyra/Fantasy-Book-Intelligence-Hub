import logging
import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DB_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "fantasy_books.db"
)

TABLE_NAME = "books"


def load_books():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}"
        )

    connection = sqlite3.connect(DB_PATH)

    try:
        query = f"""
        SELECT
            title,
            author,
            publish_year,
            language
        FROM {TABLE_NAME}
        """

        df = pd.read_sql_query(
            query,
            connection
        )

    finally:
        connection.close()

    return df


def show_metrics(df):
    total_books = len(df)

    unique_authors = df["author"].nunique()

    oldest_year = int(df["publish_year"].min())
    newest_year = int(df["publish_year"].max())

    publication_range = (
        f"{oldest_year} - {newest_year}"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📚 Total Books",
        total_books
    )

    col2.metric(
        "✍️ Authors",
        unique_authors
    )

    col3.metric(
        "📅 Publication Range",
        publication_range
    )


def show_author_chart(df):
    st.subheader("📊 Books by Author")

    author_counts = (
        df["author"]
        .value_counts()
        .sort_values(ascending=False)
    )

    st.bar_chart(author_counts)


def show_year_chart(df):
    st.subheader("📅 Books by Publication Year")

    year_counts = (
        df["publish_year"]
        .dropna()
        .astype(int)
        .value_counts()
        .sort_index()
    )

    st.bar_chart(year_counts)


def main():
    st.set_page_config(
        page_title="Fantasy Book Intelligence Hub",
        layout="wide"
    )

    st.title(
        "📚 Fantasy Book Intelligence Hub"
    )

    st.caption(
        "A fantasy and science-fiction book collection built from Open Library data."
    )

    try:
        books_df = load_books()

    except FileNotFoundError as error:
        st.error(str(error))
        return

    except Exception as error:
        st.error(
            f"Unexpected error: {error}"
        )
        return

    st.sidebar.header("Filters")

    author_options = ["All Authors"] + sorted(
        books_df["author"].unique().tolist()
    )

    selected_author = st.sidebar.selectbox(
        "Select Author",
        author_options
    )

    if selected_author == "All Authors":
        filtered_df = books_df

    else:
        filtered_df = books_df[
            books_df["author"] == selected_author
        ]

    show_metrics(filtered_df)

    st.divider()

    show_author_chart(filtered_df)

    st.divider()

    show_year_chart(filtered_df)

    st.divider()

    st.subheader("📋 Book Collection")

    st.dataframe(
        filtered_df,
        width="stretch"
    )


if __name__ == "__main__":
    main()

