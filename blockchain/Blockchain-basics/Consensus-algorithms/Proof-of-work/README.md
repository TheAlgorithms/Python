# Blockchain Summary
Congratulations! You have completed all the steps required to build a basic blockchain! In this exercise, we will bring the key parts together to review what we have built so far.

*Note: * The blockchain we have built only exists on a local machine. It is important to know that actual blockchain applications operate on multiple computers in a decentralized manner.

### Instructions


#### Step: 1
Create a Blockchain object named `local_blockchain`. Verify that this automatically creates a Genesis Block by printing out the contents of `local_blockchain`.

###### Hint:
Use the `.print_blocks()` method to print out the contents of the blockchain.

#### Step: 2
Individually add `block_one_transactions`, `block_two_transactions`, and `block_three_transactions` respectively into `local_blockchain`. Print out the contents of `local_blockchain` to see what the block holds.

###### Hint:
Use the method `.add_block(transactions)` to add blocks that contain the required transactions.

#### Step: 3
Modify the second block you added in `local_blockchain` by changing the block’s transactions to `fake_transactions`. Check to see if the blockchain is still valid using the correct method.

###### Hint:
You can access the block by indexing into `local_blockchain.chain`. You can validate the block using the `.validate_chain()` method.