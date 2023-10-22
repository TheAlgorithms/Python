import os
import requests
from bs4 import BeautifulSoup


urls_list = list()
output_dir = "extracted_articles"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def extract_article_text(url:str)->str:
    """
    This fuction takes url and extract the Title and Paragraph of the Web page and stores
    them into text file.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("title").text
        article_text = ""
        for paragraph in soup.find_all("p"):
            article_text += paragraph.text + "\n"
        return title, article_text
    else:
        return None, None


if __name__ == "__main__":
    for url in urls_list:
        title, article_text = extract_article_text(url)
        if title and article_text:
            print(f"Title is {title} ,  Article is {article_text}")
        else:
            print(f"Error extracting: {url}")
    print("Extraction complete.")
