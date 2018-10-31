print()
print('=================================================')
print('         Bem-vindo ao Jogo da Cobrinha!          ')
print('=================================================')
print()

nlinhas = int(input('Número de linhas do tabuleiro : '))
ncols   = int(input('Número de colunas do tabuleiro: '))
x0      = int(input('Posição x inicial da cobrinha : '))
y0      = int(input('posição y inicial da cobrinha : '))
t       = int(input('Tamanho da cobrinha           : '))

# Verifica se corpo da cobrinha cabe na linha do tabuleiro,
# considerando a posição inicial escolhida para a cabeça
if x0 - (t - 1) < 0:
    # Não cabe
    print()
    print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")

else:

    ''' Inicia a variável d indicando nela que t-1 partes do corpo
        da cobrinha estão inicialmente alinhadas à esquerda da cabeça.
        Exemplos:
           se t = 4, então devemos fazer d = 222
           se t = 7, então devemos fazer d = 222222
    '''
    d = 0
    i = 1
    while i <= t-1:
        d = d * 10 + 2
        i = i + 1

    # Laço que controla a interação com o jogador
    direcao = 1
    while direcao != 5:
        # mostra tabuleiro com a posição atual da cobrinha
        imprime_tabuleiro(nlinhas, ncols, x0, y0, d)

        # lê o número do próximo movimento que será executado no jogo
        print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
        direcao = int(input("Digite o número do seu próximo movimento: "))

        if direcao != 5:
            # atualiza a posição atual da cobrinha
            x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)

print()        
print("Tchau!")

# ======================================================================

def num_digitos(n):
    """ (int) -> int

    Devolve o número de dígitos de um número.

    ENTRADA
    - n: número a ser verificado 

    """
    # Escreva sua função a seguir e corrija o valor devolvido no return

    n = int(input('qual é o numero: ')) 
    num_digitos = 0
    i = 0
    while n != 0:
        i = n % 10
        n = n // 10 
        num_digitos = num_digitos + 1
        i = i + 1

    print("Número de digitos é", num_digitos)

    return num_digitos

# ======================================================================
def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    """(int, int, int, int, int, int, int) -> bool

    Devolve True se alguma parte da cobra ocupa a posição (x,y) e
    False no caso contrário.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x, y: posição a ser testada
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça

    """

    # Escreva sua função a seguir e corrija o valor devolvido no return
    Achei = False

    while (d != 0):
        resto = d % 10
        d = d // 10

        if resto == 1:
            x0 = x0 + 1

        if resto == 2:
            x0 = x0 - 1

        if resto == 3:
            y0 = y0 - 1

        if resto == 4:
            y0 = y0 + 1

        if x == x0 and y == y0:
            achei = True


    return True


# ======================================================================
def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça

    """


     # Escreva sua função a seguir
    print("Vixe! Ainda não fiz a função imprime_tabuleiro()!")



# ======================================================================
def move(nlinhas, ncols, x0, y0, d, direcao):
    """(int, int, int, int, int, int) -> int, int, int

    Move a cobra na direção dada.    
    A função devolve os novos valores de x0, y0 e d (nessa ordem).
    Se o movimento é impossível (pois a cobra vai colidir consigo mesma ou
    com a parede), então a função devolve os antigos valores e imprime a
    mensagem apropriada: "COLISÃO COM SI MESMA" ou "COLISÃO COM A PAREDE"

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    - direcao: direção na qual a cabeça deve ser movida

    """

    # Escreva sua função a seguir e corrija o valor devolvido no return
    print("Vixe! Ainda não fiz a função move()!")

    return x0, y0, d

# ======================================================================
main()   
