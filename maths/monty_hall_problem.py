from random import choice

sequence = ['a', 'b', 'c']
win = 0
lose = 0
victory = 0
defeat = 0

print('\033[01;34mSIMULAÇÃO MONTY HALL\033[m')

#escolha da porta premiada, da porta escolhida pelo competidor e da porta aberta pelo apresentador
# chose the prized door, from the door chosed by the user and the door opened by the holst

for c in range(1, 1000):
    car = choice(sequence)
    chose = choice(sequence)
    remove = car
    while remove == car or remove == chose:
        remove = choice(sequence)

#troca de portas
#change door

    change = choice(sequence)
    while change == remove or change == chose:
        change = choice(sequence)

    chose = choice(sequence)
    while chose == remove:
        chose = choice(sequence)

#contabilizando as vitórias e derrotas
#couting wins and loses

    if change == car:
        win += 1
    else:
        lose += 1

    if chose == car:
        victory += 1
    else:
        defeat += 1

#exibindo resultados
#show results

print('\n\033[01;32mWith change:\033[m ')
print(f'Win: {win}\nLose: {lose}')

print('\n\033[01;31mWithout change:\033[m ')
print(f'Win: {victory}\nLose: {defeat}')

