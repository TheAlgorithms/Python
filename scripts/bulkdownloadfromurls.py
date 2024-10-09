import os
import requests
from urllib.parse import urlsplit, quote_plus
import pandas as pd


def read_urls_from_csv(csv_file, column_name):
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Extract URLs from specified column
        urls = df[column_name].tolist()

        return urls
    except Exception as e:
        print(f"Error reading URLs from CSV: {e}")
        return []


def download_image(url, folder):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Generate a unique filename using the URL
        filename = quote_plus(url)  # Encode URL to use as filename
        filename = filename[:25]  # Limit filename length (optional)
        filename = f"{filename}.jpg"  # Add file extension if needed

        # Create the output path
        output_path = os.path.join(folder, filename)

        # Save the image to the specified folder
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(8192):
                file.write(chunk)

        print(f"Downloaded: {url} to {output_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")


def download_images_from_list(url_list, folder):
    # Create the output folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    for url in url_list:
        download_image(url, folder)


if __name__ == "__main__":
    # CSV file containing URLs
    csv_file = "your_csv"
    column_name = (
        "YOUR COLUMN LINK CONTAING URLS"  # Replace with the column name containing URLs
    )

    # Read URLs from CSV
    image_urls = read_urls_from_csv(csv_file, column_name)

    # Folder to save downloaded images
    output_folder = "downloaded_images"

    # Download images
    download_images_from_list(image_urls, output_folder)
