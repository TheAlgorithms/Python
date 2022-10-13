# Contributed by @Shah-Aayush
# Basic Blockchain implementation
"""
- implemented concepts :
	- reward mechanism
	- proof of work
	- chain validation
	- adding/viewing specific blocks of blockchain
	- hashing mechanism and generation of hash values
"""

import datetime
import hashlib
import json
import random

# import JSON
# from flask import jsonify

# def compute_hash(index, previous_hash, timestamp, data):
#     return hashlib.sha256((str(index) + str(previous_hash) + str(timestamp) + json.dumps(data)).encode('utf-8')).hexdigest()


def compute_hash(hash_data:str) -> str:
    """ computes hash value """
    return hashlib.sha256(hash_data.encode("utf-8")).hexdigest()

def proof_of_work(hash_data:str, difficulty:int) -> (str, int, int):
    """ computes proof of work for given data and difficulty level """
    nonce = 1
    if difficulty == -1:
        difficulty = random.randint(1, 5)
    print("current difficulty level is : ", difficulty)
    while True:
        temp_hash = compute_hash(hash_data + str(nonce))
        if temp_hash[:difficulty] == "0" * difficulty:
            break
        nonce += 1
    return temp_hash, nonce, difficulty


class Block:
    """ Class to generate individual block """
    def __init__(self, index:int, data:str, previous_hash:str, reward:int) -> None:
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = str(datetime.datetime.now())
        hash_data = (
            str(self.index)
            + str(self.previous_hash)
            + str(self.timestamp)
            + json.dumps(self.data)
        )
        self.hash, self.nonce, self.difficulty = proof_of_work(hash_data, -1)
        self.reward = reward

    def print_block_details(self) -> None:
        print(f"Details for block indexed at {self.index} : ")
        print(f"\tData : {self.data}")
        print(f"\tTimeStamp : {self.timestamp}")
        print(f"\tHash : {self.hash}")
        print(f"\tPrevious Hash : {self.previous_hash}")
        print(f"\tReward : {self.reward}")
        print(f"\tNonce : {self.nonce}")
        print(f"\tDifficulty : {self.difficulty}")


class BlockChain:
    """ Class for blockchain """
    # chain = []
    def __init__(self, total_reward:int, partician:int) -> None:
        """ constructor """
        self.chain = []
        self.partician = partician
        self.total_reward = total_reward - partician
        genesis_block = Block(
            len(self.chain) + 1, "Aayush's BlockChain!", 0, self.partician
        )
        self.chain.append(genesis_block)

    def add_block(self, data:str) -> None:
        """ class for adding block to the chain """
        assigned_reward = 0
        if self.total_reward - self.partician > 0:
            self.total_reward -= self.partician
            assigned_reward = self.partician
        elif self.total_reward > 0:
            assigned_reward = self.total_reward
            self.total_reward = 0
        new_block = Block(
            len(self.chain) + 1, data, self.chain[-1].hash, assigned_reward
        )
        self.chain.append(new_block)

    def get_previous_block(self) -> Block:
        """ returns last block """
        return self.chain[-1]

    def get_specific_block(self, index:int) -> Block:
        """ returns specific block according to given index """
        return self.chain[index]

    def print_block(self, block:Block) -> None:
        """ prints block details for given block """
        block.print_block_details()

    def chain_validation(self) -> bool:
        """ validates hash values of the chain """
        hash_data, _, __ = proof_of_work(
            str(self.chain[0].index)
            + str(self.chain[0].previous_hash)
            + str(self.chain[0].timestamp)
            + json.dumps(self.chain[0].data),
            self.chain[0].difficulty,
        )
        if self.chain[0].hash != hash_data:
            return False
        print("\t> genesis block is validated.")
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i - 1].hash:
                return False
            hash_data, _, __ = proof_of_work(
                str(self.chain[i].index)
                + str(self.chain[i].previous_hash)
                + str(self.chain[i].timestamp)
                + json.dumps(self.chain[i].data),
                self.chain[i].difficulty,
            )
            if self.chain[i].hash != hash_data:
                return False
            if (
                i != len(self.chain) - 1
                and self.chain[i].hash != self.chain[i + 1].previous_hash
            ):
                return False
            print(f"\t> {i+1}th block is validated.")
        return True


if __name__ == "__main__":
    """ main menu driven function """
    total_reward = int(input("Enter total reward you want to assign your chain : "))
    partician = total_reward
    while partician >= total_reward:
        partician = int(
            input(
                "Enter partician reward value which will be assingned to each block : "
            )
        )
        if partician >= total_reward:
            print("Partician value should be less then reward value.")

    my_block_chain = BlockChain(total_reward, partician)

    while True:
        print(
            """MENU :
    1. Add block
    2. View Specific block
    3. View Last block
    4. Validate chain
    5. Exit"""
        )
        choice = int(input("Choice : "))
        # try:
        if choice == 1:
            data = input("\t\tEnter data for the block : ")
            my_block_chain.add_block(data)
            print(f"Added block at index {len(my_block_chain.chain)}")
        elif choice == 2:
            index = int(input("\t\tEnter block index : "))
            try:
                my_block_chain.print_block(my_block_chain.get_specific_block(index - 1))
            except:
                print("# Invalid index entered!")
        elif choice == 3:
            my_block_chain.print_block(my_block_chain.get_previous_block())
        elif choice == 4:
            if my_block_chain.chain_validation():
                print(f"\tChain is validated.")
            else:
                print(f"\tChain is not validated")
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("# Invalid choice!")
        # except:
        #     print('# Integer value expected!')
