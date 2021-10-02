import praw

# creating an instance for praw reddit
# get all the user cridentials form the reddit page: https://www.reddit.com/prefs/apps
reddit = praw.Reddit(
    # Client ID
    client_id="Enter client id here",
    # Client Secret Key
    client_secret="Enter client secret here",
    # User Agent
    user_agent="Enter user agent here",
    check_for_async=False
)


def crawler(subreddit: str)-> list[str]:
    """
    Crawls the data and prints them
    """
    data = []
    hot = reddit.subreddit(subreddit).hot(limit=100)
    for post in hot:
        data.append(post.title)
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    data = crawler("all")
    print(data)
