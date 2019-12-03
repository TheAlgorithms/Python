from math import ceil
from hashlib import sha256

def fdh(string, n: int = 256):
    '''
    full domain hash of 'string' using SHA256 with digest of n-1 bits.
    Generates a hash with an arbitrary bit size given as input (n)
    The function generates a hash digest of bitsize = n bits.   
    This is achieved by repeatedly appending an incremental value at the
    end of input string and calculation of SHA256 hash. These hash
    digests are concatenated to generate hash of desired bit size
    '''
    
    result = []
    
    for i in range(ceil(n/256)): #produce enough sha256 digests to make total 'n' bit composite digest
        
        result.append( sha256((string+str(i)).encode()).hexdigest() ) #Appends an integer incrementally to the message & generates its hash
        
    result = ''.join(result)   #Combine all the hashes generated.
    
    return result
