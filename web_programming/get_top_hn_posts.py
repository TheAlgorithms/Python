import requests
from texttable import Texttable


def hackernews_top_stories(max_stories: int = 10) -> dict:
    """
    Get the top 10 posts from HackerNews and display
    them as a table inside the terminal
    https://news.ycombinator.com/
    """

    top_stories = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

    top_10 = requests.get(top_stories).json()[:10]

    table_data = [
        ["Title", "URL"],
    ]

    for story_id in top_10:
        story_url = (
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
        )
        story_content = requests.get(story_url).json()
        content = [story_content["title"], story_content["url"]]
        table_data.append(content)

    table = Texttable()
    table.set_cols_dtype(["t", "a"])
    table.add_rows(table_data)
    print(table.draw())


if __name__ == "__main__":
    stories()
