transaction1 = {"amount": "20", "sender": "Add", "receiver": "White"}
transaction2 = {"amount": "200", "sender": "White", "receiver": "Add"}
transaction3 = {"amount": "300", "sender": "Alice", "receiver": "Timothy"}
transaction4 = {"amount": "300", "sender": "Rodrigo", "receiver": "Thomas"}
transaction5 = {"amount": "200", "sender": "Timothy", "receiver": "Thomas"}


mempool = [transaction1, transaction2, transaction3, transaction4, transaction5]

# add your code below
my_transaction = {"amount": "500", "sender": "name_1", "receiver": "name_2"}

mempool.append(my_transaction)

block_transactions = [transaction1, transaction3, my_transaction]
