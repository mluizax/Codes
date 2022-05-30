a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

delta = (b ** 2) - 4 * a * c

print(f'\nO valor de delta será {delta}')
print('\nA operação está sendo realizada...\n')

if a == 0:
    print('O valor de "a" deve ser diferente de 0')
elif delta < 0:
    print('Não existem raízes reais')
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f'Primeiro valor encontrado para x: {x1}\nSegundo valor encontrado para x: {x2}')
