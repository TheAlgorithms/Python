import os
import requests
from bs4 import BeautifulSoup

# Read the input file
url_list = list()
with open("url.txt", "r") as f:
    url_list = f.read().split("\n")
    f.close()


# Create a directory to save the extracted articles
output_dir = "extracted_articles"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Function to extract article text
def extract_article_text(url):
    """
    This fuction takes url and extract the Title and Paragraph of the Web page and stores
    them into text file.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # to extract the title and article text
        title = soup.find("title").text
        article_text = ""
        for paragraph in soup.find_all("p"):
            article_text += paragraph.text + "\n"
        return title, article_text
    else:
        return None, None


# Looping through the URLs in the DataFrame URL_ID
for url in url_list:
    title, article_text = extract_article_text(url)
    if title and article_text:
        # Generate a unique file name using URL_ID
        file_name = os.path.join(output_dir, str(url.split("/")[3] + ".txt"))
        # Write the title and article text to the file
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            f.write(article_text)
        print
    else:
        print(f"Error extracting: {url} with id :{url_id}")

print("Extraction and saving complete.")
