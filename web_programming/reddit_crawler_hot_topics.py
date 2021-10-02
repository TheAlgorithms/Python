import praw

# creating an instance for praw reddit
# get all the user cridentials form the reddit page: https://www.reddit.com/prefs/apps and enter below
reddit = praw.Reddit(
    client_id="Enter client id here",
    client_secret="Enter client secret here",
    user_agent="Enter user agent here",
    check_for_async=False
)


def crawler(subreddit: str) -> list[str]:
    """
    >>> crawler("all")
    ["abcd","hijk","lmn","op","qr"]
    """
    hot = reddit.subreddit(subreddit).hot(limit=5)
    data = list(map(lambda post: post.title, hot))
    return data


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    data = crawler("all")
    print(data)
