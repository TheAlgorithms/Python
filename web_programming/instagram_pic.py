from datetime import UTC, datetime

import requests
from bs4 import BeautifulSoup


def resim_indir(url: str) -> str:
    """
    Verilen bir URL'den 'og:image' meta etiketini kazıyarak bir resim indirin.

    Parametreler:
        url: Kazınacak URL.

    Dönüş:
        İşlemin sonucunu belirten bir mesaj.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"{url} adresine yapılan HTTP isteği sırasında bir hata oluştu: {e!r}"

    soup = BeautifulSoup(response.text, "html.parser")
    image_meta_tag = soup.find("meta", {"property": "og:image"})
    if not image_meta_tag:
        return "'og:image' özelliğine sahip meta etiketi bulunamadı."

    image_url = image_meta_tag.get("content")
    if not image_url:
        return f"Meta etiketinde resim URL'si bulunamadı {image_meta_tag}."

    try:
        image_data = requests.get(image_url, timeout=10).content
    except requests.exceptions.RequestException as e:
        return f"{image_url} adresine yapılan HTTP isteği sırasında bir hata oluştu: {e!r}"
    if not image_data:
        return f"{image_url} adresinden resmi indirme başarısız oldu."

    file_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H:%M:%S}.jpg"
    with open(file_name, "wb") as out_file:
        out_file.write(image_data)
    return f"Resim indirildi ve {file_name} dosyasına kaydedildi."


if __name__ == "__main__":
    url = input("Resim URL'sini girin: ").strip() or "https://www.instagram.com"
    print(f"resim_indir({url}): {resim_indir(url)}")
