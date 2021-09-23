#Solution to project euler problem 1
def sum(mul):
    multiples_of_3 = []
    multiples_of_5 = []
    for elements in mul:
        if elements % 3 == 0:
            multiples_of_3.append(elements)
        elif elements % 5 == 0:
            multiples_of_5.append(elements)
        else:
            break
    sum_of_all = multiples_of_3 + multiples_of_5
    print(sum_of_all)
sum(list(range(1, 1000)))
#Can anyone plz tell where am i mistaken?
