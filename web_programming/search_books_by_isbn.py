"""
Get book and author data from https://openlibrary.org

ISBN: https://en.wikipedia.org/wiki/International_Standard_Book_Number
"""

from json import JSONDecodeError  # Workaround for requests.exceptions.JSONDecodeError

import requests


def get_openlibrary_data(olid: str = "isbn/0140328726") -> dict:
    """
    Given an 'isbn/0140328726', return book data from Open Library as a Python dict.
    Given an '/authors/OL34184A', return authors data as a Python dict.
    This code must work for olids with or without a leading slash ('/').

    # Comment out doctests if they take too long or have results that may change
    # >>> get_openlibrary_data(olid='isbn/0140328726')  # doctest: +ELLIPSIS
    {'publishers': ['Puffin'], 'number_of_pages': 96, 'isbn_10': ['0140328726'], ...
    # >>> get_openlibrary_data(olid='/authors/OL7353617A')  # doctest: +ELLIPSIS
    {'name': 'Adrian Brisku', 'created': {'type': '/type/datetime', ...
    """
    new_olid = olid.strip().strip("/")  # Remove leading/trailing whitespace & slashes
    if new_olid.count("/") != 1:
        msg = f"{olid} is not a valid Open Library olid"
        raise ValueError(msg)
    return requests.get(f"https://openlibrary.org/{new_olid}.json", timeout=10).json()


def summarize_book(ol_book_data: dict) -> dict:
    """
    Given Open Library book data, return a summary as a Python dict.
    """
    desired_keys = {
        "title": "Title",
        "publish_date": "Publish date",
        "authors": "Authors",
        "number_of_pages": "Number of pages:",
        "first_sentence": "First sentence",
        "isbn_10": "ISBN (10)",
        "isbn_13": "ISBN (13)",
    }
    data = {better_key: ol_book_data[key] for key, better_key in desired_keys.items()}
    data["Authors"] = [
        get_openlibrary_data(author["key"])["name"] for author in data["Authors"]
    ]
    data["First sentence"] = data["First sentence"]["value"]
    for key, value in data.items():
        if isinstance(value, list):
            data[key] = ", ".join(value)
    return data


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    while True:
        isbn = input("\nEnter the ISBN code to search (or 'quit' to stop): ").strip()
        if isbn.lower() in ("", "q", "quit", "exit", "stop"):
            break

        if len(isbn) not in (10, 13) or not isbn.isdigit():
            print(f"Sorry, {isbn} is not a valid ISBN.  Please, input a valid ISBN.")
            continue

        print(f"\nSearching Open Library for ISBN: {isbn}...\n")

        try:
            book_summary = summarize_book(get_openlibrary_data(f"isbn/{isbn}"))
            print("\n".join(f"{key}: {value}" for key, value in book_summary.items()))
        except JSONDecodeError:  # Workaround for requests.exceptions.RequestException:
            print(f"Sorry, there are no results for ISBN: {isbn}.")
