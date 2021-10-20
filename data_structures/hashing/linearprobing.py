import numpy as np

# Linear probing program
class Hash_table() :
    
    def __init__(self,size) :
      """
      :param size=intger
      """
        self.size = size
        self.hashtable = np.array([None]*self.size)
        
    def hash(self,key: int) -> int:
        """
        Hash function h(x) = x%10
        returns the index of the hashtable
        :param key value
        """
        index = key%10 
        
        if self.hashtable[index] == None :
            return index
        else :
            
            # Implementing linear probing
            while self.hashtable[index] != None :
                index = (index+1)%10
                
            return index
        
    def insert(self,key: int):
        """
        this function inserts an element into the hash table.
        :param: key
        """
        index = self.hash(key)
        self.hashtable[index] = key
        
    def search(self,key: int) -> int:
        """
        searching the key element present in the hash table or not
        returns: index of the element (if founded)
                 else None
        """
        index = key%10
        
        if self.hashtable[index] != key :
            while self.hashtable[index] != key and self.hashtable[index] != None :
                index = (index+1)%10
                
        if self.hashtable[index] == key :
            return index
        else :
            return None
    
    def print_hashtable(self) :
        """
        prints the hash table when called
        """
        print("Hash table is :-\n\nindex \t value")
        for x in range(len(self.hashtable)) :
            print(x,"\t",self.hashtable[x])

# Initializing hash table of size 10
HT = Hash_table(10)

# Inserting only 5 values to make λ <= 0.5
HT.insert(10)
HT.insert(90)
HT.insert(25)
HT.insert(5)
HT.insert(35)

HT.print_hashtable()

index = HT.search(35)

if index!= None :
    print("\nGiven key is present at index",index)
else :
    print("\nGiven key is not present in the hash table")
