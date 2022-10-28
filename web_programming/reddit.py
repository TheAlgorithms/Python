from __future__ import annotations

import requests

valid_terms = set(
    """approved_at_utc approved_by author_flair_background_color
author_flair_css_class author_flair_richtext author_flair_template_id author_fullname
author_premium can_mod_post category clicked content_categories created_utc downs
edited gilded gildings hidden hide_score is_created_from_ads_ui is_meta
is_original_content is_reddit_media_domain is_video link_flair_css_class
link_flair_richtext link_flair_text link_flair_text_color media_embed mod_reason_title
name permalink pwls quarantine saved score secure_media secure_media_embed selftext
subreddit subreddit_name_prefixed subreddit_type thumbnail title top_awarded_type
total_awards_received ups upvote_ratio url user_reports""".split()
)


def get_subreddit_data(
    subreddit: str, limit: int = 1, age: str = "new", wanted_data: list | None = None
) -> dict:
    """
    subreddit : Subreddit to query
    limit : Number of posts to fetch
    age : ["new", "top", "hot"]
    wanted_data : Get only the required data in the list
    """
    wanted_data = wanted_data or []
    if invalid_search_terms := ", ".join(sorted(set(wanted_data) - valid_terms)):
        raise ValueError(f"Invalid search term: {invalid_search_terms}")
    response = requests.get(
        f"https://reddit.com/r/{subreddit}/{age}.json?limit={limit}",
        headers={"User-agent": "A random string"},
    )
    if response.status_code == 429:
        raise requests.HTTPError

    data = response.json()
    if not wanted_data:
        return {id_: data["data"]["children"][id_] for id_ in range(limit)}

    data_dict = {}
    for id_ in range(limit):
        data_dict[id_] = {
            item: data["data"]["children"][id_]["data"][item] for item in wanted_data
        }
    return data_dict


if __name__ == "__main__":
    # If you get Error 429, that means you are rate limited.Try after some time
    print(get_subreddit_data("learnpython", wanted_data=["title", "url", "selftext"]))
