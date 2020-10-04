import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def youtube_scraper():

    """
    Returns a pandas dataframe consisting of links, views, likes, dislikes and
    their date of upload of the first 500 vidoes appearing in the user's feed
    """

    browser = webdriver.Chrome(
        executable_path="chromedriver", options=webdriver.ChromeOptions()
    )
    home_page = "https://www.youtube.com"
    browser.get(home_page)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    raw_links = []
    while True:
        browser.get(home_page)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        links_tag = soup.find_all(
            "a", class_="yt-simple-endpoint style-scope ytd-rich-grid-video-renderer"
        )
        try:
            raw_links += list(
                map(lambda x: "https://youtube.com" + x["href"], links_tag)
            )[1::2]
        except Exception:
            pass
        if len(raw_links) > 500:
            break

    views = []
    dates = []
    likes = []
    dislikes = []
    links = []
    for link in raw_links:
        browser.get(link)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        view_tag = soup.find_all("span", class_="view-count")
        date_tag = soup.find_all("div", id="date")
        like_dislike_tag = soup.find_all(
            "yt-formatted-string",
            class_="style-scope ytd-toggle-button-renderer style-text",
        )
        try:
            views.append(view_tag[0].text.split()[0])
            dates.append(date_tag[0].text[1:])
            likes.append(like_dislike_tag[0]["aria-label"].split()[0])
            dislikes.append(like_dislike_tag[1]["aria-label"].split()[0])
            links.append(link)
        except Exception:
            roll_back = min(
                len(views), len(dates), len(likes), len(dislikes), len(link)
            )
            views = views[:roll_back]
            dates = dates[:roll_back]
            likes = likes[:roll_back]
            dislikes = dislikes[:roll_back]
            links = links[:roll_back]

    df = pd.DataFrame(
        {
            "links": links[:500],
            "views": views[:500],
            "date": dates[:500],
            "likes": likes[:500],
            "dislikes": dislikes[:500],
        }
    )
    return df


if __name__ == "main":
    df = youtube_scraper()
    df.to_csv("youtube_output.csv", index=False)
