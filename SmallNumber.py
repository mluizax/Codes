list_one = [1, 2, 3, 4, 5, 6]
list_two = [22, 50, 13, 5, 9, 150]
list_three = [5, 9, 3]


def buscarMenor(list):
    menor = list[0]
    for elemento in list:
        if elemento < menor:
            menor = elemento
    print('O menor valor da lista é: ', menor)


buscarMenor(list_one)
buscarMenor(list_two)
buscarMenor(list_three)
