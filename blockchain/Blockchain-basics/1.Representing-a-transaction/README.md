# Building a Transaction Representation

Welcome to this hands-on lesson where you'll embark on the journey of constructing your own blockchain in Python! This tutorial assumes a prior understanding of Python syntax, functions, loops, library imports, and class construction. However, we've included some hints along the way to assist you. If you're new to Python, you may find it beneficial to [acquire some foundational Python knowledge through geeksforgeeks](https://www.geeksforgeeks.org/python-programming-language/)

## The Role of Transactions

Blockchain technology introduces a novel approach to securely store and transmit data. Most notably, it excels at managing transactions, which involve exchanges of information between two parties. Before we dive into the creation of our blockchain, let's consider an effective way to represent a transaction like the one illustrated below:

**Transaction Representation**

Consider the following transaction details:

- **Amount:** 20
- **Sender:** Add
- **Receiver:** White

In this scenario, Add aims to transfer 20 units of a particular currency to White. To represent this transaction effectively in Python, we opt for a data type that suits its structure.

The ideal choice for representing such transactions is by utilizing a Python dictionary. This dictionary can hold keys corresponding to the essential fields and values that contain transaction-specific information.

These transactions are commonly stored within a component known as the "mempool." The mempool serves as a reservoir of pending transactions, which miners consult when determining the set of transactions they intend to validate.


### Instructions

#### Step 1: Creating a Transaction

To begin, let's craft a transaction and incorporate it into the `mempool`. We'll name this new transaction `my_transaction` and assign key-value pairs for `amount`, `sender`, and `receiver`.

**Hint:** In Python, you can create a dictionary using the following syntax: `dictionary = {}`

#### Step 2: Joining the Mempool

Next, let's include `my_transaction` within the `mempool` list.

**Hint:** You can add an item to a Python list using the following syntax: `list.append(element)`

#### Step 3: Compiling Block Transactions

Now, create a fresh list named `block_transactions` and populate it with three transactions sourced from the `mempool`. This step will prepare the transactions for future integration into our evolving Block structure.

By following these steps, you'll gain hands-on experience in managing transactions within the blockchain and laying the groundwork for their incorporation into Blocks.

