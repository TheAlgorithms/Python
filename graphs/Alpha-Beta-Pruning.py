tree = {
    'A':['B','C','D'],
    'B':['E','F'],
    'C':['G','H','I'],
    'D':['J','K'],
    'E':[],
    'F':[],
    'G':[],
    'H':['L','M'],
    'I':['N','O'],
    'L':[],
    'M':[],
    'N':[],
    'O':[],
    'J':[],
    'K':[]
}

utility = {
    'E':4,
    'F':5,
    'G':6,
    'L':3,
    'M':4,
    'N':7,
    'O':9,
    'J':3,
    'K':8
}

def TerminalTest(state):
    if len(tree[state])==0:
        return True
    return False

def Utility(state):
    return utility[state]

def ACTION(state):
    return tree[state]

def ABS(state):
    v=MAX_VALUE(state,float('-inf'),float('inf'))
    return v

def MAX_VALUE(state,alpha,beta):
    if TerminalTest(state):
        return Utility(state)
    v = float('-inf')
    for action in ACTION(state):
        v=max(v,MIN_VALUE(action,alpha,beta))
    if v>= beta:
        return v
    alpha = max(alpha,v)
    return v
    
def MIN_VALUE(state,alpha,beta):
    if TerminalTest(state):
        return Utility(state)
    v = float('inf')
    for action in ACTION(state):
        v=min(v,MAX_VALUE(action,alpha,beta))
    if v>= alpha:
        return v
    beta = min(beta,v)
    return v    


print(ABS('A'))
