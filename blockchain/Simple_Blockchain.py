import datetime
import hashlib
import json

chain = []


def create_block(proof,previous_hash):
        block = {'index': len(chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof':proof,
                 'previous_hash': previous_hash}

        chain.append(block)

        return block

create_block(proof=1, previous_hash='0')

def print_previous_block():
    return chain[-1]

def proof_of_work(previous_proof):
    new_proof = 1
    check_proof = False

    while check_proof is False:
        hash_operation = hashlib.sha256(
            str(new_proof**2 - previous_proof**2).encode()).hexdigest()
        if hash_operation[:4] == '00000':
            check_proof = True

        else:
            new_proof +=1

        return new_proof

def hash(block):
    encoded_block = json.dumps(block,sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()

def chain_valid(chain):
    previous_block = chain[0]
    block_index = 1

    while block_index < len(chain):
        block = chain[block_index]
        if block['previous_hash'] != hash(previous_block):
            return False
               
        previous_proof = previous_block['proof']
        proof = block['proof']
        hash_operation = hashlib.sha256(
            str(proof**2 - previous_proof**2).encode()).hexdigest()
             
        if hash_operation[:4] != '00000':
            return False
        previous_block = block
        block_index += 1

    



if __name__ == '__main__':

    def mine_block():
        previous_block = print_previous_block()
        previous_proof = previous_block['proof']
        proof = proof_of_work(previous_proof)
        previous_hash = hash(previous_block)
        block = create_block(proof, previous_hash)
     
        response = {
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']}
        
        print(response)


    def display_chain():
        response = {'chain': chain,
                'length': len(chain)}
        print(response)

    def valid():
        valid = chain_valid(chain)
        if valid:
            response = {'The Blockchain is valid.'}
        else:
            response = {'The Blockchain is not valid'}
        print(response)

    print("MINED BLOCK")
    mine_block()
    print("DISPLAY CHAIN")
    display_chain()
    print("VALID")
    valid()
    


    

    

        

