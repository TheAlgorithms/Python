def checksub(T, P):
    for i in range(len(T)-len(P)+1):
        b = T[i:len(P)+i]
        if P == b:
            return True
    return False


a = "abcdefghijklmnopqrstuvwxyz"
b = "mnopi"
print(checksub(a, b))

# T(n)=O(len(P),len(T))
# This is a naive algorithm
