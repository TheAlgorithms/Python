'''
    Number of turns it takes it takes to move n rings across 3 rods A,B and C from source rod A to destination rod C.  
'''
def tower_of_hanoi(n, source, destination, aux):
    if(n == 1):
        print("Move disk ",n," from ", source, " to ",destination)
        return
    tower_of_hanoi(n-1,source, aux, destination)
    print("Move disk ",n," from ",source," to ",destination)
    tower_of_hanoi(n-1,aux,destination,source)

n = 5
tower_of_hanoi(n,'A','B','C')