def TOH(n, S, M, D):
    if(n==1):
        print("Move disk {} from {} to {}".format(n,S,D))
        return 0
    TOH( n-1, S, D, M)
    print("Move disk {} from {} to {}".format(n,S,D))
    TOH(n-1, M, S, D)

if __name__ == "__main__":
    print("Enter no. of disks")
    n = int(input())
    TOH(n,'A','B','C')
