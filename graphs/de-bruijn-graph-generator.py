
from itertools import permutations
#De brujin graph via matrix

alpha_bet = ['a','b','c']


def generate_de_bruijn_graph(alphaBet,n):
    return list(permutations(alphaBet,len(alphaBet)))
    pass



##Tests...
print(generate_de_bruijn_graph(alphaBet,2))

print("###################################3")

print(generate_de_bruijn_graph(alphaBet,3))
