table = [[]]
itens = {}
W = 0

def knapsack(i, W):
    global itens, table
    if (i < 1):
        return 0
    if (itens[i]['weight'] > W):
        table[i][W-1] = knapsack(i - 1, W)
        return table[i][W-1]
    else:
        table[i][W-1] = max(knapsack(i - 1, W), itens[i]['value'] + knapsack(i - 1, W - itens[i]['weight']))
        return table[i][W-1]

def printItens(n, W):
    global table, itens
    res = table[n][W-1]
    print('Maior valor possível: ' + str(res))
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i -1][w-1]:
            continue
        else:
            # Este item está incluso
            print(itens[i]['name'])
             
            # Quando incluso o vlaor e o peso são deduzidos
            res = res - itens[i]['value']
            w = w - itens[i]['weight']


def printLine(W):
    print(" ", end="")
    for i in range(W + 1):
        print("-----",end="")
    print("")

def printKnapsack(W):
    global table
    print("\nKnapsack Table:")
    printLine(W+3)
    print("|{0:20}|".format("itens           peso"), end="")
    for i in range(0, W):
        print("{0: >3} |".format(i+1), end="")
    print("")
    printLine(W+3)
    for i in range(len(itens)):
        print("|{0:13}({1:2},{2:2})|".format(itens[i+1]['name'], itens[i+1]['value'], itens[i+1]['weight']), end="")
        for j in range(W):
            print("{0: >3} |".format(table[i+1][j]), end="")
        print("")
        printLine(W+3)

def readItens():
    global itens, W
    print('Digite a capacidade da mochila: ', end='')
    W = int(input())
    print('Digite a quantidade de itens: ', end='')
    numItens = int(input())
    for i in range(numItens):
        print('Digite o nome do item ' + str(i+1) + ':', end='')
        name = input()
        print('Digite o peso do item ' + str(i+1) + ':', end='')
        weight = int(input())
        print('Digite o valor do item ' + str(i+1) + ':', end='')
        value = int(input())
        itens[i+1] = {'value': value, 'weight': weight, 'name': name}



def main():
    global table, itens, W
    readItens()
    # Inicializa tabela com 0's
    table = [[0 for i in range(W)] for i in range(len(itens)+1)]
    for i in range(len(itens)+1):
        for j in range(W):
            table[i][j] = 0
    # Preenche tabela
    print("Result: {}".format(knapsack(len(itens), W)))
    printKnapsack(W)
    printItens(len(itens), W)

if __name__ == '__main__':
    main()
