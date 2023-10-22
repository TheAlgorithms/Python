"""
This script demonstrates how to interact with the EOSIO blockchain using the eosfactory library in Python. It deploys the blog_contract to the blockchain and performs various actions such as initializing a blog, signing up a user, and creating a new post. Make sure to configure the connection to your EOSIO node and the required account information before running this script.

"""

from eosfactory.eosf import *

# Setup the EOSIO workspace
reset()

create_master_account("master")

create_account("blog", master)
blog = Account("blog")

# Define the blog contract
blog_contract = Contract(blog, "blog_contract")
blog_contract.build(force=True)
blog_contract.deploy()

# Define the actions
initblog_action = blog_contract.initblog(authority)
signupuser_action = blog_contract.signupuser(authority, "John Doe", "avatar.png")
createpost_action = blog_contract.createpost(
    authority, "First Post", "Hello World!", user
)

# Push the actions to the blockchain
initblog_action.push()
signupuser_action.push()
createpost_action.push()
