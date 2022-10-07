def kineticEnergy(M, V):
 
    
    KineticEnergy = 0.5 * M * V * V
 
    return KineticEnergy
 

def potentialEnergy(M, H):
 
    
    PotentialEnergy = M * 9.8 * H
 
    return PotentialEnergy
 
# Driver Code
if __name__ ==  "__main__":
 
    M = 5.5
    H = 23.5
    V = 10.5
 
    print("Kinetic Energy = ", kineticEnergy(M, V))
    print("Potential Energy = ", potentialEnergy(M, H))
    
    
