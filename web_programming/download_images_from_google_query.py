import json
import os
import re
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup

# Kullanıcı ajanı başlıkları
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def download_images_from_google_query(query: str = "dhaka", max_images: int = 5) -> int:
    """
    Sağlanan arama terimini kullanarak Google'da arama yapar ve resimleri bir klasöre indirir.

    Args:
        query : Kullanıcı tarafından sağlanacak resim arama terimi. Varsayılan "dhaka".
        max_images : İndirilecek maksimum resim sayısı. Varsayılan 5.

    Returns:
        Başarıyla indirilen resim sayısı.
    """
    max_images = min(max_images, 50)  # Kötüye kullanımı önlemek için!
    params = {
        "q": query,
        "tbm": "isch",
        "hl": "en",
        "ijn": "0",
    }

    # Google arama sonuçlarını al
    html = requests.get(
        "https://www.google.com/search", params=params, headers=headers, timeout=10
    )
    soup = BeautifulSoup(html.text, "html.parser")
    
    # Resim verilerini ayıkla
    matched_images_data = "".join(
        re.findall(r"AF_initDataCallback\(([^<]+)\);", str(soup.select("script")))
    )

    # JSON verilerini düzelt ve yükle
    matched_images_data_fix = json.dumps(matched_images_data)
    matched_images_data_json = json.loads(matched_images_data_fix)

    # Google resim verilerini ayıkla
    matched_google_image_data = re.findall(
        r"\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",",
        matched_images_data_json,
    )
    if not matched_google_image_data:
        return 0

    # Küçük resimleri kaldır
    removed_matched_google_images_thumbnails = re.sub(
        r"\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]",
        "",
        str(matched_google_image_data),
    )

    # Tam çözünürlüklü resimleri ayıkla
    matched_google_full_resolution_images = re.findall(
        r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
        removed_matched_google_images_thumbnails,
    )
    
    # Resimleri indir
    for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
        if index >= max_images:
            return index
        original_size_img_not_fixed = bytes(fixed_full_res_image, "ascii").decode(
            "unicode-escape"
        )
        original_size_img = bytes(original_size_img_not_fixed, "ascii").decode(
            "unicode-escape"
        )
        opener = urllib.request.build_opener()
        opener.addheaders = [
            (
                "User-Agent",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
            )
        ]
        urllib.request.install_opener(opener)
        path_name = f"query_{query.replace(' ', '_')}"
        if not os.path.exists(path_name):
            os.makedirs(path_name)
        urllib.request.urlretrieve(  # noqa: S310
            original_size_img, f"{path_name}/original_size_img_{index}.jpg"
        )
    return index

if __name__ == "__main__":
    try:
        image_count = download_images_from_google_query(sys.argv[1])
        print(f"{image_count} images were downloaded to disk.")
    except IndexError:
        print("Please provide a search term.")
        raise
