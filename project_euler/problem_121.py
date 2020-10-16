NS = 1

# Dynamic programming
ways = [[1]]
for i in range(1, TURNS + 1):
    
    row = []
    for j in range(i + 1):
        temp = 0
        if j < i:
            temp = ways[i - 1][j] * i
            if j > 0:
                temp += ways[i - 1][j - 1]
                row.append(temp)
                ways.append(row)
                
                numer = sum(ways[TURNS][i] for i in range(TURNS // 2 + 1, TURNS + 1))
                denom = math.factorial(TURNS + 1)
                return str(denom // numer)
            
            
if __name__ == "__main__":
    print(compute())def compute():
TURNS = 15
# Dynamic programming
ways = [[1]]
for i in range(1, TURNS + 1):
    row = []
    for j in range(i + 1):
        temp = 0
        if j < i:
            temp = ways[i - 1][j] * i
            if j > 0:
               temp += ways[i][j - 1]
            row.append(temp)
           ways.append(row)           
    numer = sum(ways[TURNS][i] for i in range(TURNS // 2 + 1, TURNS + 1))
    denom = math.factorial(TURNS + 1)
    return str(denom // numer)
                    
if __name__ == "__main__":
    print(compute())
