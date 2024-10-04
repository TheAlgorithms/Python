"""
Get book and author data from https://openlibrary.org

ISBN: https://en.wikipedia.org/wiki/International_Standard_Book_Number
"""

from json import JSONDecodeError  # Workaround for requests.exceptions.JSONDecodeError

import requests


def get_openlibrary_data(olid: str = "isbn/0140328726") -> dict:
    """
    Verilen 'isbn/0140328726' ile Open Library'den kitap verilerini Python dict olarak döndürür.
    Verilen '/authors/OL34184A' ile yazar verilerini Python dict olarak döndürür.
    Bu kod, başında veya sonunda eğik çizgi ('/') olan veya olmayan olids için çalışmalıdır.

    # Doctest'leri yorum satırı yapın eğer çok uzun sürüyorsa veya sonuçlar değişebilir.
    # >>> get_openlibrary_data(olid='isbn/0140328726')  # doctest: +ELLIPSIS
    {'publishers': ['Puffin'], 'number_of_pages': 96, 'isbn_10': ['0140328726'], ...
    # >>> get_openlibrary_data(olid='/authors/OL7353617A')  # doctest: +ELLIPSIS
    {'name': 'Adrian Brisku', 'created': {'type': '/type/datetime', ...
    """
    new_olid = olid.strip().strip("/")  # Başındaki/sonundaki boşlukları ve eğik çizgileri kaldır
    if new_olid.count("/") != 1:
        msg = f"{olid} geçerli bir Open Library olid değil"
        raise ValueError(msg)
    return requests.get(f"https://openlibrary.org/{new_olid}.json", timeout=10).json()


def summarize_book(ol_book_data: dict) -> dict:
    """
    Verilen Open Library kitap verilerini özet olarak Python dict şeklinde döndürür.
    """
    desired_keys = {
        "title": "Başlık",
        "publish_date": "Yayın tarihi",
        "authors": "Yazarlar",
        "number_of_pages": "Sayfa sayısı",
        "first_sentence": "İlk cümle",
        "isbn_10": "ISBN (10)",
        "isbn_13": "ISBN (13)",
    }
    data = {better_key: ol_book_data[key] for key, better_key in desired_keys.items()}
    data["Yazarlar"] = [
        get_openlibrary_data(author["key"])["name"] for author in data["Yazarlar"]
    ]
    data["İlk cümle"] = data["İlk cümle"]["value"]
    for key, value in data.items():
        if isinstance(value, list):
            data[key] = ", ".join(value)
    return data


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    while True:
        isbn = input("\nAramak için ISBN kodunu girin (veya 'quit' yazarak çıkın): ").strip()
        if isbn.lower() in ("", "q", "quit", "exit", "stop"):
            break

        if len(isbn) not in (10, 13) or not isbn.isdigit():
            print(f"Üzgünüz, {isbn} geçerli bir ISBN değil. Lütfen geçerli bir ISBN girin.")
            continue

        print(f"\nOpen Library'de ISBN: {isbn} aranıyor...\n")

        try:
            book_summary = summarize_book(get_openlibrary_data(f"isbn/{isbn}"))
            print("\n".join(f"{key}: {value}" for key, value in book_summary.items()))
        except JSONDecodeError:  # requests.exceptions.RequestException için geçici çözüm
            print(f"Üzgünüz, ISBN: {isbn} için sonuç bulunamadı.")
