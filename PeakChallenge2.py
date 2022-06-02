# Método número 2 para resolver o Desafio 1 - Algoritmo Peak Finding

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

print(biggerValue)


biggerValue = list_two[0]
while count < len(list_two):
    currentValue = list_two[count]

    if(biggerValue < currentValue):
        biggerValue = currentValue
    count += 1
print(biggerValue)


biggerValue = list_three[0]
while count < len(list_three):
    currentValue = list_three[count]

    if(biggerValue < currentValue):
        biggerValue = currentValue
    count += 1
print(biggerValue)


biggerValue = list_four[0]
while count < len(list_four):
    currentValue = list_four[count]

    if(biggerValue < currentValue):
        biggerValue = currentValue
    count += 1
print(biggerValue)
