import copy
import sys


def createM(alphabet):
    M = []
    smallst = []   
    
    graph = [
        [0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 0]]
    #create the basic graph
    for i in range(0, len(graph)):
        #print(graph2[i])
        for j in range(0, len(graph[i])):
            if(graph[i][j] > 0):#there is an edge
                if(i != j):#remove the self-loops
                    smallst.append(alphabet[j])            

        M.append(smallst)
        smallst = []  
            
    return M




def creatingM1(M, alphabet):
    newM = copy.deepcopy(M)

    countLines = 0
    for i in newM:
        count = 0
        for j in i:
            newM[countLines][count] =  alphabet[countLines]+ j
            count += 1
        countLines += 1
        
    return newM



def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    M = createM(alphabet)#a list with the starting graph without the self-loops
    
    newM = creatingM1(M, alphabet)#newM have paths that can become a Hamiltonian circle
    
    repeats = 0
    #finding Hamiltonian paths
    while (repeats < len(newM) - 2):
        localHP = []
        for i in newM:
            smallPath = []
            for j in i:
                #this alphabet.find(j[len(j)-1]) is for geting the position of a letter
                for k in M[alphabet.find(j[len(j)-1])]:
                    if(j.find(k)<0):
                        smallPath.append(j + k)
            
            localHP.append(smallPath)
        newM = []
        newM = copy.deepcopy(localHP)
        
        repeats += 1
    

    #finding Hamiltonian circles
    
    for i in newM:
        smallPath = []
        for j in i:
            for k in M[alphabet.find(j[len(j)-1])]:
                if(j[0] == k):
                    smallPath.append(j+k)
    
    
    if (len(smallPath) == 0):
        print("No Hamiltonian circle. Exit program")
        sys.exit()
    
    print("The Hamiltonian circles are:")
    print(smallPath)
    
    
    aHamiltonianCircle = smallPath[0]
    SmallerM = copy.deepcopy(M)
    
    print("We will work with this Hamiltonian circle:")
    print(aHamiltonianCircle)
    #remove the paths from Hamiltonian circle
    for i, j in zip(aHamiltonianCircle[:len(aHamiltonianCircle) - 1], aHamiltonianCircle[1:]):
        SmallerM[alphabet.find(i)].remove(j)
        SmallerM[alphabet.find(j)].remove(i)
    

    #Creates the A group, and B group/ inside and outside
    A = []
    B = []
    
    Adone = True
    j = 0
    whatGoesToA = 0
    #we look at the available path of the starting node of the Hamiltonian circle
    
    while (j < len(aHamiltonianCircle) and Adone):
        if (len(SmallerM[alphabet.find(aHamiltonianCircle[j])])> 0):
            Adone = False
            whatGoesToA = j
            for i in SmallerM[alphabet.find(aHamiltonianCircle[j])]:#Creates A 
                A.append(aHamiltonianCircle[j] + i) 
                SmallerM[alphabet.find(i)].remove(aHamiltonianCircle[j])
                
        j += 1

    if (Adone):
        print("There is no possible path for creating the group A. The graph is a level graph ")
        sys.exit()
        
    j -= 1
    SmallerM[alphabet.find(aHamiltonianCircle[j])] = []
    Bdone = True
    j = 0
    #we look at the available path of the second node of the Hamiltonian circle
    while (j < len(aHamiltonianCircle) and Bdone):
        if (len(SmallerM[alphabet.find(aHamiltonianCircle[j])])> 0) and (j!=whatGoesToA):
            Bdone = False
            for i in SmallerM[alphabet.find(aHamiltonianCircle[j])]:#Creates B
                B.append(aHamiltonianCircle[j] + i)
                SmallerM[alphabet.find(i)].remove(aHamiltonianCircle[j])
        j += 1
    

    if (Bdone):
        print("There is no possible path for creating the group B. This is a level graph ")
        sys.exit()
    
    j -= 1
    SmallerM[alphabet.find(aHamiltonianCircle[j])] = []
    
    i = 0
    #we look at the rest of the nodes in the Hamiltonian circle

    while i < len(SmallerM):
        if (len(SmallerM[i])>0):
            #slicing the Hamilton path
            for j in SmallerM[i]:
                #First Letter = alphabet[i]
                #Second Letter = j
                x = aHamiltonianCircle.find(alphabet[i])
                y = aHamiltonianCircle.find(j)
                if x < y:
                    TempPath = aHamiltonianCircle[x + 1:y]
                else:
                    TempPath = aHamiltonianCircle[y + 1:x]
                
                aDone = True
                
                for a in A:
                    if (
                        (TempPath.find(a[0]) >= 0) and not (a[1] == alphabet[i] or a[1] == j)
                        or 
                        (TempPath.find(a[1]) >= 0) and not (a[0] == alphabet[i] or a[0] == j)
                        ):
                        aDone = False

                 
                if (aDone):
                    A.append(alphabet[i] + j)
                    SmallerM[alphabet.find(j)].remove(alphabet[i])
                
                bDone = True
                if(not aDone):
                    for b in B:
                        if (
                            (TempPath.find(b[0]) >= 0) and not (b[1] == alphabet[i] or b[1] == j )
                            or 
                            (TempPath.find(b[1]) >= 0) and not (b[0] == alphabet[i] or b[0] == j )
                            ):
                            bDone = False
                    
                    if(bDone):
                        B.append(alphabet[i] + j)
                        SmallerM[alphabet.find(j)].remove(alphabet[i])
                
                
                if(not aDone and not bDone):
                    print("This is not level graph ")
                    sys.exit()
                
        i += 1
                
    
    print("This is a level graph, the two groups of edges are: ")
    print(A)
    print(B)    




if (__name__ == "__main__"):
    main() #ABCDEFGHI
