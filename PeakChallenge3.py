# Método número 2 para resolver o Desafio 1 - Algoritmo Peak Finding
# Aqui é mostrado apenas do índice do item de maior valor de cada lista
# Para o código ficar melhor, posso criar uma função e chamá-la a cada lista

list_one = [1, 2, 3]
list_two = [2, 3, 1]
list_three = [3, 2, 1]
list_four = [1, 2, 3, 1, 5]

count = 0

biggerValue = list_one[0]

while count < len(list_one):
    currentValue = list_one[count]

    if(biggerValue < currentValue):
        biggerValue = currentValue
    count += 1

print(list_one.index(biggerValue))


count = 0
biggerValue = list_two[0]
while count < len(list_two):
    currentValue = list_two[count]

    if(biggerValue < currentValue):
        biggerValue = currentValue
    count += 1
print(list_two.index(biggerValue))

count = 0
biggerValue = list_three[0]
while count < len(list_three):
    currentValue = list_three[count]

    if(biggerValue < currentValue):
        biggerValue = currentValue
    count += 1
print(list_three.index(biggerValue))

count = 0
biggerValue = list_four[0]
while count < len(list_four):
    currentValue = list_four[count]

    if(biggerValue < currentValue):
        biggerValue = currentValue
    count += 1
print(list_four.index(biggerValue))
