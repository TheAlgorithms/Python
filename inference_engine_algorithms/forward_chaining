import re


def find_symbols_in_kb(knowledge_base: list[str]) -> dict:
    '''
    '''
    inferred = {}

    for i in range(len(knowledge_base)):
        symbols = re.findall(r'[a-zA-Z]', knowledge_base[i])
        for symbol in symbols:
            if symbol not in inferred:
                inferred[symbol] = False

    return inferred


def number_of_symbols_in_premise(knowledge_base: list[str]) -> dict:

    '''
    '''

    count = {}
    for clause in knowledge_base:
        if(len(clause) != 1):
            index = clause.find("=>")
            premise = clause[:index]
            letters = ''.join(e for e in premise if e.isalpha())
            count[premise] = len(letters)

    return count


def get_known_facts(knowledge_base: list[str]) -> list[str]:

    '''
    '''
    facts = []
    for clause in knowledge_base:
        if len(clause) == 1:
            facts.append(clause)

    return facts




def forward_chianing(knowledge_base: list[str], query:str) -> bool:

    count = number_of_symbols_in_premise(knowledge_base)
    inferred = find_symbols_in_kb(knowledge_base)
    queue = get_known_facts(knowledge_base)

    while(len(queue) > 0):
        p = queue.pop()
        if p == query: return True
        if inferred[p] == False:
            inferred[p] = True
            for clause in knowledge_base:
                index = clause.find("=>")
                premise = clause[:index]
                if p in premise:
                    count[premise] -= 1
                    if count[premise] == 0:
                        queue.append(clause[-1])

    return False



if __name__ == "__main__":

    kb = ["p => q", "q => r", "r => p", "s => t", "u => v", "v => w", "w => u", "a", "b", "c" , "w" , "u&q=>r", "q"]

    result = forward_chianing(kb, "p")
    print(result)