
from itertools import permutations
#De brujin graph via matrix

alpha_bet = ['a','b','c']


def generate_de_bruijn_graph(alphaBet,n):
    return list(permutations(alpha_bet,len(alpha_bet)))
    pass



##Tests...
print(generate_de_bruijn_graph(alpha_bet,2))

print("###################################3")

print(generate_de_bruijn_graph(alpha_bet,3))
