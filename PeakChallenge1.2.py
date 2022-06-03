# Método número 1 para resolver o Desafio 1 - Algoritmo Peak Finding
# Criação de uma função para obter os resultados

print('Valores de pico de cada lista e seu respectivo índice:')

list_one = [1, 2, 3]
list_two = [2, 3, 1]
list_three = [3, 2, 1]
list_four = [1, 2, 3, 1, 5]


def get_max_value(list):
    max_value = max(list)
    print(f'\nMaior valor da lista: {max_value}\nÍndice: {list.index(max_value)}')


get_max_value(list_one)

get_max_value(list_two)

get_max_value(list_three)

get_max_value(list_four)
