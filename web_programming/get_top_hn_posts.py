import requests


def hackernews_top_stories(max_stories: int = 10) -> int:
    """
    Get the top 10 posts from HackerNews and display
    them as a table inside the terminal
    https://news.ycombinator.com/
    
    >>> max_stories = 10
    >>> hackernews_top_stories(max_stories)
    10
    
    >>> max_stories = 5
    >>> hackernews_top_stories(max_stories)
    5
    """

    top_stories = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

    top_10 = requests.get(top_stories).json()[:max_stories]

    table_data = []

    for story_id in top_10:
        story_url = (
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
        )
        story_content = requests.get(story_url).json()
        content = [story_content["title"], story_content["url"]]
        table_data.append(content)

    for row in table_data:
        print(f"{'-' * 150} \n | {row[0]} \n | {row[1]}")

    return len(table_data)


if __name__ == "__main__":
    hackernews_top_stories()
