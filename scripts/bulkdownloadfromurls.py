import os
import requests
from urllib.parse import quote_plus
import pandas as pd

def read_urls_from_csv(csv_file, column_name):
    try:
        # Read CSV file into a DataFrame
        image_data = pd.read_csv(csv_file)

        # Extract URLs from specified column
        urls = image_data[column_name].tolist()

        return urls
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []
    except ValueError as e:
        print(f"Error processing CSV: {e}")
        return []

def download_image(url, folder):
    try:
        # Send a GET request to the URL with a timeout
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        # Generate a unique filename using the URL
        filename = quote_plus(url)[:25]  # Limit filename length
        filename = f"{filename}.jpg"

        # Create the output path
        output_path = os.path.join(folder, filename)

        # Save the image to the specified folder
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(8192):
                file.write(chunk)

        print(f"Downloaded: {url} to {output_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def download_images_from_list(url_list, folder):
    os.makedirs(folder, exist_ok=True)
    for url in url_list
        download_image(url, folder)

if __name__ == "__main__":
    csv_file = "face_dataset.csv"
    column_name = "Imagelink"
    image_urls = read_urls_from_csv(csv_file, column_name)
    output_folder = "downloaded_images"
    download_images_from_list(image_urls, output_folder)
