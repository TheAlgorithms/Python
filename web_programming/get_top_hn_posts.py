from __future__ import annotations

import requests


def get_hackernews_story(story_id: str) -> dict:
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"İstek hatası: {e}"}
    except ValueError as e:
        return {"error": f"JSON ayrıştırma hatası: {e}"}


def hackernews_top_stories(max_stories: int = 10) -> list[dict]:
    """
    HackerNews'ten en fazla max_stories gönderiyi alın - https://news.ycombinator.com/
    """
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        story_ids = response.json()[:max_stories]
        return [get_hackernews_story(story_id) for story_id in story_ids]
    except requests.exceptions.RequestException as e:
        return [{"error": f"İstek hatası: {e}"}]
    except ValueError as e:
        return [{"error": f"JSON ayrıştırma hatası: {e}"}]


def hackernews_top_stories_as_markdown(max_stories: int = 10) -> str:
    stories = hackernews_top_stories(max_stories)
    return "\n".join(
        "* [{title}]({url})".format(**story) if "title" in story and "url" in story else "* Hata: {error}".format(**story)
        for story in stories
    )


if __name__ == "__main__":
    print(hackernews_top_stories_as_markdown())
