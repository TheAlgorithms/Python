# Building Blocks

Now, let's consider an effective approach to represent a block in Python. Instead of using a large dictionary to store our data, we can leverage object-oriented programming principles and create a Block Class. This Block Class will facilitate the straightforward creation of new blocks.

Remember that a Block encompasses the following fundamental properties:

Timestamp
Transaction
Hash
Previous Hash
Nonce
In this exercise, we'll be crafting the default constructor for the Block class within our Mini-Blockchain.

# Building Blocks and Managing Timestamps

In this guide, you will learn how to incorporate timestamps and initialize a Block class for your Mini-Blockchain project.

## Introduction

A blockchain relies on the structured arrangement of blocks, each containing vital information. We'll work on integrating timestamps into your blockchain and create a Block class to store essential blockchain data.

### Step 1: Importing the `datetime` Module

Every `Block` in the blockchain is associated with a timestamp, representing its creation time. To generate this timestamp dynamically, we need to import the `datetime` module from the `datetime` library.

**Hint:** To make a module accessible in your code, you must import it from the respective library. Use the following format to import a specific module:

```python
from datetime import datetime

#### Step: 2
Inside the [datetime module](https://docs.python.org/2/library/datetime.html) there is a `.now()` method that returns the current date and time.

Call the `datetime` module’s `.now()` method to print out the current date and time.

###### Hint:
The appropriate way to call this method is `datetime.now()` enclosed in a `print()` statement.

#### Step: 3
Now let’s work on creating our `Block`. We will be passing `transactions` and `previous_hash` to the default constructor each time a `Block` is created.

Complete the `__init__()` method inside the Block class by initializing the following instance variables:

- `transactions`
- `previous_hash`
- `nonce` (with a default value of `0`).

###### Hint:
The header for the function should look as follows:

`def __init__(self, transactions, previous_hash, nonce = 0):`

Be sure to initialize all the variables as well:

```def __init__(self, value):
  # Initialization:
  self.value = value```

#### Step: 4
Inside the `__init__()` method, create a `timestamp` instance variable that stores the current date and time.

###### Hint:
Call the `.now()` method from the `datetime` module and store the result in `timestamp`.




