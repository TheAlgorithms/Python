from web3 import Web3
import json


ganache_url = "GANACHE_SERVER"
#
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "ACCOUNT_1_Address"
account_2 = "ACCOUNT_2_Address"

private_key = "Private_Key_of_Sender"

#get the nonce

nonce = web3.eth.getTransactionCount(account_1)

# build the transaction
tx = {
    'nonce' : nonce,
    'to' : account_2,
    'value' : web3.toWei(1, 'ether'),
    'gas' : 2000000,
    'gasPrice' : web3.toWei('50', 'gwei')
}

# sign the transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# get the transaction hash
print(tx_hash)




