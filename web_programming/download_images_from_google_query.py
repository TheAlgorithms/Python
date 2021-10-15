import requests
import re
import json
import urllib.request
from bs4 import BeautifulSoup
import os
import sys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    + " (KHTML, like Gecko)"
    + "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}
max_image = 999


def download_images_from_google_query(
    query: str = "dhaka", image_numbers: int = 5
) -> bool:
    """Searches google using the provided query term and downloads the images in a folder.

    Args:
         query : The image search term to be provided by the user. Defaults to
        "dhaka".
        image_numbers : [description]. Defaults to 5.

    Returns:
        True if the image is downloaded successfully.

    >>> download_images_from_google_query ()
    True
    >>> download_images_from_google_query ("potato")
    True
    """

    params = {
        "q": query,
        "tbm": "isch",
        "hl": "en",
        "ijn": "0",
    }

    html = requests.get("https://www.google.com/search", params=params, headers=headers)
    soup = BeautifulSoup(html.text, "lxml")
    matched_images_data = "".join(
        re.findall(r"AF_initDataCallback\(([^<]+)\);", str(soup.select("script")))
    )

    matched_images_data_fix = json.dumps(matched_images_data)
    matched_images_data_json = json.loads(matched_images_data_fix)

    matched_google_image_data = re.findall(
        r"\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",",
        matched_images_data_json,
    )
    if not len(matched_google_image_data):
        return False
    removed_matched_google_images_thumbnails = re.sub(
        r"\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]",
        "",
        str(matched_google_image_data),
    )

    matched_google_full_resolution_images = re.findall(
        r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
        removed_matched_google_images_thumbnails,
    )
    for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
        if index == image_numbers or index == max_image:
            return True
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
                + " (KHTML, like Gecko)"
                + "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
            )
        ]
        urllib.request.install_opener(opener)
        if not os.path.exists("query-" + query):
            os.makedirs("query-" + query)
        urllib.request.urlretrieve(
            original_size_img, f"query-{query}/original_size_img_{index}.jpg"
        )
    return True


if __name__ == "__main__":
    try:
        download_images_from_google_query(sys.argv[1])
    except IndexError:
        print("Please provide a search term.")
        raise
