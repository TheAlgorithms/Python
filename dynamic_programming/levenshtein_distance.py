"""
LEVENSHTEIN DISTANCE dyamic programming implementation to show the difference between two strings (https://en.wikipedia.org/wiki/Levenshtein_distance)
"""

def levenshtein_distance(str_a, str_b):
    len_a = len(str_a)+1
    len_b = len(str_b)+1
    distance_matrix = [[-1 for i in range(len_b)] for i in range(len_a)] #make matrix of size len_a+1 x len_b+1
    for i in range(len_a):
        distance_matrix[i][0] = i
    for j in range(len_b):
        distance_matrix[0][j] = j
    for i in range(1, len_a):
        for j in range(1, len_b):
            if str_a[i-1] == str_b[j-1]:
                cost = 0
            else:
                cost = 1
            distance_matrix[i][j] = min(distance_matrix[i-1][j], distance_matrix[i][j-1], distance_matrix[i-1][j-1]) + cost
    return distance_matrix[len_a-1][len_b-1]
    
# example - expected answer = 2 (1 substitution + 1 deletion)
print(levenshtein_distance("GAMBOL", "GUMBO"))
