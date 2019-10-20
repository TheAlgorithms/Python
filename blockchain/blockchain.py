from block import Block
import datetime
num_blocks_to_add = int(input("Please enter the number of blocks to add: ").strip())
block_chain = [Block.create_genesis_block()]
print("The genensis block has been created!")
print("Hash: %s"%block_chain[0].hash)

for i in range(1,num_blocks_to_add):
    block_chain.append(Block(block_chain[i-1].hash,"Block number %d"%i,datetime.datetime.now()))
    print("Block #%d created."%i)
    print("Hash: %s"%block_chain[-1].hash)
"""
Blocks are created according to the input given.

Please enter the number of blocks to add: 8
The genensis block has been created!
Hash: c3aef6564b4ed4444afc18a2484c7b495d3ec14d34432991d7539b8d04798393
Block #1 created.
Hash: ec5bba233b21745d2e41db87a6612c18d8cec6aacb3f2eb2bb75cc7030b3615b
Block #2 created.
Hash: f0d3fadd2532b4dc9f95bf156af5b1aea7e55951f2e054e1c02f6a94897f3d3a
Block #3 created.
Hash: 9869c261ed078be898de4eec4b51025bfbb4e1440ba5e8bd21d94328081a8cbc
Block #4 created.
Hash: 70210ae34059bc70f70772b5c783e27857b415f275465701ad02007d78ab972e
Block #5 created.
Hash: b0e3db6060e288a29548697e3a16b7b8bd32a005979513357ece390928ceffdf
Block #6 created.
Hash: b542517a6a5891765acc38135b647d9fe2a6704648e8222fa6b03c0c7bbf7105
Block #7 created.
Hash: 2c13cf5e87d6f5f06bade3826ad3fa964320361ea499915234abb8566fc588e4

"""