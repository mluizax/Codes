number_one = input('Escolha o primeiro número: ')
number_two = input('Escolha o segundo número: ')
number_one = int(number_one)
number_two = int(number_two)

if number_two == number_one**2:
    print(f'{number_two} é raiz quadrada de {number_one}.')
else:
    print(f'{number_two} NÃO é raiz quadrada de {number_one}.')
