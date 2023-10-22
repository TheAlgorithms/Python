"""
the following code i'm writing is just a DEMONSTARTION OF HOW ONE CAN WRITE A SMART CONTRACT IN PYTHON USING 'NEAR' PROTOCOL.
"""

import near
from near import account, Contract, view, post, setup

setup("testnet")  # Replace with 'mainnet' for mainnet deployment


# Initialize the contract
@post
def init_blog(authority: str):
    blogs[0] = {"blog_id": 0, "current_post_key": 0, "authority": authority}


# Sign up a user
@post
def signup_user(authority: str, name: str, avatar: str):
    user_id = len(users) + 1
    users[user_id] = {
        "user_id": user_id,
        "name": name,
        "avatar": avatar,
        "authority": authority,
    }


# Create a new post
@post
def create_post(authority: str, title: str, content: str, user: str):
    assert len(blogs) > 0, "Blog does not exist. Initialize the blog first."
    post_id = len(posts) + 1
    posts[post_id] = {
        "post_id": post_id,
        "title": title,
        "content": content,
        "user": user,
        "pre_post_key": blogs[0]["current_post_key"],
        "authority": authority,
    }
    blogs[0]["current_post_key"] = post_id


# Initialize the NEAR account and deploy the contract
account = near.Account("your_account_id")
contract = Contract(
    account, "blog_contract", "blog.wasm", setup, "Your NEAR Access Key"
)

# Access the contract functions
init_blog = contract.init_blog("your_authority_account_id")
signup_user = contract.signup_user(
    "your_authority_account_id", "John Doe", "avatar.png"
)
create_post = contract.create_post(
    "your_authority_account_id", "First Post", "Hello World!", "user_id"
)

# Push the transactions to the NEAR blockchain
init_blog.apply()
signup_user.apply()
create_post.apply()
