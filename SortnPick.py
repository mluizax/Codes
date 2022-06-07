list = [1, 55, 178, 53, 3, 9, 1500, 97]

for number in range(0, len(list)):
    for item in range(number, len(list)):
        if list[number] > list[item]:
            list[number], list[item] = list[item], list[number]

print(f'A lista em ordem crescente será: {list}')
print(f'O segundo maior valor da lista será: {list[-2]}')
