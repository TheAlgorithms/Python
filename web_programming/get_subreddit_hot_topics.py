import praw

# Create an praw.Reddit instance containing the credentials required for API access.
# Get the required user credentials from https://www.reddit.com/prefs/apps
reddit = praw.Reddit(
    client_id="Enter client id here",
    client_secret="Enter client secret here",
    user_agent="Enter user agent here",
    check_for_async=False
)


def get_subreddit_hot_topics(subreddit: str, limit: int = 5) -> list[str]:
    """
    Return the titles of up to limit hot topics in the provided subreddit.
    
    >>> crawler("all")
    ["abcd","hijk","lmn","op","qr"]
    """
    return [post.title for post in reddit.subreddit(subreddit).hot(limit=limit)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(get_subreddit_hot_topics("all"))
