# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


def download_images_from_google_query(query: str = "dhaka", max_images: int = 5) -> int:
    """
    Searches google using the provided query term and downloads the images in a folder.

    Args:
         query : The image search term to be provided by the user. Defaults to
        "dhaka".
        image_numbers : [description]. Defaults to 5.

    Returns:
        The number of images successfully downloaded.

    # Comment out slow (4.20s call) doctests
    # >>> download_images_from_google_query()
    5
    # >>> download_images_from_google_query("potato")
    5
    """
    max_images = min(max_images, 50)  # Prevent abuse!
    params = {
        "q": query,
        "tbm": "isch",
        "hl": "en",
        "ijn": "0",
    }

    html = httpx.get(
        "https://www.google.com/search", params=params, headers=headers, timeout=10
    )
    soup = BeautifulSoup(html.text, "html.parser")
    matched_images_data = "".join(
        re.findall(r"AF_initDataCallback\(([^<]+)\);", str(soup.select("script")))
    )

    matched_images_data_fix = json.dumps(matched_images_data)
    matched_images_data_json = json.loads(matched_images_data_fix)

    matched_google_image_data = re.findall(
        r"\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",",
        matched_images_data_json,
    )
    if not matched_google_image_data:
        return 0

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
        # Sanitise the query so it cannot escape the output directory.
        # Replace any character that is not alphanumeric, space, hyphen, or
        # underscore with an underscore, then collapse spaces.
        safe_query = re.sub(r"[^\w\s-]", "_", query).replace(" ", "_")
        output_dir = Path.cwd() / f"query_{safe_query}"
        output_dir.mkdir(parents=True, exist_ok=True)
        # Resolve to an absolute path and verify it stays inside cwd.
        dest = (output_dir / f"original_size_img_{index}.jpg").resolve()
        if not str(dest).startswith(str(Path.cwd().resolve())):
            raise ValueError(f"Refusing to write outside working directory: {dest}")
        urllib.request.urlretrieve(  # noqa: S310
            original_size_img, dest
        )
    return index


if __name__ == "__main__":
    try:
        image_count = download_images_from_google_query(sys.argv[1])
        print(f"{image_count} images were downloaded to disk.")
    except IndexError:
        print("Please provide a search term.")
        raise
