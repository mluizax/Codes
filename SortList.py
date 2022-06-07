list = []

for item in range(0, 6):
    number = int(
        input('Digite até seis números para salvar em ordem crescente: '))
    if item == 0 or number > list[-1]:
        list.append(number)
    else:
        position = 0
        while position < len(list):
            if number <= list[position]:
                list.insert(position, number)
                break
            position += 1

print(f'Os números escolhidos em ordem crescente: {list}')
print(f'O segundo maior valor da lista é {list[-2]}')
print(f'O segundo menor valor da lista é {list[1]}')
