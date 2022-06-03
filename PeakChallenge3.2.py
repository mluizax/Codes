# Método número 2 para resolver o Desafio 1 - Algoritmo Peak Finding
# Criação de uma função para obter o índice do maior valor de cada lista

list_one = [1, 2, 3]
list_two = [2, 3, 1]
list_three = [3, 2, 1]
list_four = [1, 2, 3, 1, 5]


def get_max_value(list):
    count = 0
    biggerValue = list[0]
    while count < len(list):
        currentValue = list[count]
        if(biggerValue < currentValue):
            biggerValue = currentValue
        count += 1
    print(list.index(biggerValue))


get_max_value(list_one)

get_max_value(list_two)

get_max_value(list_three)

get_max_value(list_four)
