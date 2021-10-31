from logging import raiseExceptions

import requests


def get_data(
    sub: str, limit: int = 1, age: str = "new", wanted_data: list = []
) -> dict:
    """
    sub : Subreddit to query
    limit : Number of posts to fetch
    age : ["new", "top", "hot"]
    wanted_data : Get only the required data in the list
    Possible values:
        [
            'approved_at_utc', 'subreddit', 'selftext',
            'author_fullname', 'saved', mod_reason_title',
            'gilded', 'clicked', 'title', 'link_flair_richtext',
            'subreddit_name_prefixed', 'hidden', 'pwls',
            'link_flair_css_class', 'downs', 'top_awarded_type',
            'hide_score', 'name', 'quarantine', 'link_flair_text_color',
            'upvote_ratio', 'author_flair_background_color',
            'subreddit_type', 'ups', 'total_awards_received',
            'media_embed', 'author_flair_template_id',
            'is_original_content', 'user_reports', 'secure_media',
            'is_reddit_media_domain', 'is_meta', 'category',
            'secure_media_embed', 'link_flair_text', 'can_mod_post',
            'score', 'approved_by', 'is_created_from_ads_ui',
            'author_premium', 'thumbnail', 'edited',
            'author_flair_css_class', 'author_flair_richtext',
            'gildings', 'content_categories','url', 'is_video',
            'created_utc', 'permalink'
        ]
    """
    response = requests.get(f"https://reddit.com/r/{sub}/{age}.json?limit={limit}")
    if response.raise_for_status():
        raiseExceptions

    data = response.json()
    data_dict = {}

    if wanted_data == []:
        for id_ in range(limit):
            data_dict[id_] = data["data"]["children"][id_]
    else:
        for id_ in range(limit):
            singleton = {}
            for item in wanted_data:
                singleton[item] = data["data"]["children"][id_]["data"][item]

            data_dict[id_] = singleton

    return data_dict


if __name__ == "__main__":
    # If you get Error 429, that means you are rate limited.Try after some time
    print(get_data("learnpython", wanted_data=["title", "url", "selftext"]))
