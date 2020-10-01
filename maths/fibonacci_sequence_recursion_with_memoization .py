# Fibonacci Sequence Using Recursion and Memoization

cache = dict() #Cria um dicionário que guardará os resultados dos números já calculados para melhorar a perfomance.
def recur_fibo(n):
    """
    >>> [recur_fibo(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    aux = n

    if aux in cache: #Verifica se este número já foi calculado anteriormente, para avaliar se é necessário calcular seu valor fibonacci novamente.
        return cache[aux] #Existindo, o seu valor fibonacci é retornado

    if (n == 0) or (n == 1): #Caso pertença a um caso base, ele guarda o "n" em uma variavel auxiliar.("Ans -> Answer")
        ans = n
    else:
        ans = recur_fibo(n-1) + recur_fibo(n-2) #Caso não pertença a um caso base, ele faz uma chamada recursiva, guardando seu retorno na variavel "Ans"
    cache[aux] = ans #A resposta é guardada no dicionário.

    return ans    #E por fim, e retornado para o user.


def main() -> None:
    limit = int(input("How many terms to include in fibonacci series: "))
    if limit > 0:
        print(f"The first {limit} terms of the fibonacci series are as follows:")
        print([recur_fibo(n) for n in range(limit)])
    else:
        print("Please enter a positive integer: ")


if __name__ == "__main__":
    main()
