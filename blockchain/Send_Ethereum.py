"""
Importing some revelant libraries 

If you don't have web3 then you can install in Python by running command **pip install web3**

"""

from web3 import Web3
import json

"""
Ganache Server :: HTTP://127.0.0.1:7545
Basically Ganache Server will provide you accounts for practice, learn and implement.
We first connect with Ganache Server.
"""
ganache_url = "GANACHE_SERVER"

"""
Here is how we can connect with Server
"""
web3 = Web3(Web3.HTTPProvider(ganache_url))

"""
We have to provide the account details like 
Account 1 - Sender address
Account 2 - Receiver address
"""

account_1_address = "ACCOUNT_1_Address"
account_2_address = "ACCOUNT_2_Address"


"""
Doing any transaction, we have to do specify the priavte key of sender like we tranact amount through Google Pay then after giving amount it will ask about UPI Pin that's same thing here.
private key - Sender's Private key address

"""
private_key_address = "Private_Key_of_Sender"

"""
We have to get the nonce of the account like how many transactions.
"""
nonce = web3.eth.getTransactionCount(account_1_address)

"""
Build the Transcation
"""
transaction = {
    'nonce' : nonce,
    'to' : account_2,
    'value' : web3.toWei(1, 'ether'),
    'gas' : 2000000,
    'gasPrice' : web3.toWei('50', 'gwei')
}

"""
Sign the transaction
"""
signed_tranaction = web3.eth.account.signTransaction(transaction, private_key_address)


"""
Sign the Transaction
"""
transaction_hash = web3.eth.sendRawTransaction(signed_tranaction.rawTransaction)

"""
Get the hash of Transactiona and print hash.
"""
print(transaction_hash)




