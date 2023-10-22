'''
blockchain smart contracts in Python using various blockchain platforms and frameworks.
'''
from web3 import Web3
from solcx import compile_standard

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

contract_source_code = '''
pragma solidity ^0.8.0;

contract BlogContract {
    struct Blog {
        uint256 blogId;
        uint256 currentPostKey;
        address authority;
    }

    struct User {
        uint256 userId;
        string name;
        string avatar;
        address authority;
    }

    struct Post {
        uint256 postId;
        string title;
        string content;
        address user;
        uint256 prePostKey;
        address authority;
    }

    mapping(uint256 => Blog) public blogs;
    mapping(uint256 => User) public users;
    mapping(uint256 => Post) public posts;

    function initBlog(address authority) public {
        require(blogs[0].authority == address(0), "Blog already initialized");
        blogs[0] = Blog(0, 0, authority);
    }

    function signUpUser(address authority, string memory name, string memory avatar) public {
        uint256 userId = users[0].userId + 1;
        users[userId] = User(userId, name, avatar, authority);
    }

    function createPost(address authority, string memory title, string memory content, address user) public {
        require(blogs[0].authority != address(0), "Blog does not exist. Initialize the blog first.");
        uint256 postId = posts[0].postId + 1;
        posts[postId] = Post(postId, title, content, user, blogs[0].currentPostKey, authority);
        blogs[0].currentPostKey = postId;
    }
}
'''

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"blog_contract.sol": {"content": contract_source_code}},
    "settings":
        {"outputSelection": {
            "*": {"*": ["metadata", "evm.bytecode", "evm.bytecode.sourceMap"]}
        }}
})

bytecode = compiled_sol['contracts']['blog_contract.sol']['BlogContract']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['blog_contract.sol']['BlogContract']['metadata']['output']['abi']

account_address = w3.eth.accounts[0]
BlogContract = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = BlogContract.constructor().transact({'from': account_address})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

contract_address = tx_receipt.contractAddress
