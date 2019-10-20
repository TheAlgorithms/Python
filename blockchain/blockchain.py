from bc import Block
import datetime
num_blocks_to_add = 10
block_chain = [Block.create_genesis_block()]
print("The genensis block has been created!")
print("Hash: %s"%block_chain[0].hash)

for i in range(1,num_blocks_to_add):
    block_chain.append(Block(block_chain[i-1].hash,"Block number %d"%i,datetime.datetime.now()))
    print("Block #%d created."%i)
    print("Hash: %s"%block_chain[-1].hash)