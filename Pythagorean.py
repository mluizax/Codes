import math

co = int(input('Insira o valor do cateto oposto: '))
ca = int(input('Insira o valor do cateto adjacente: '))

hipotenusa = float((ca ** 2 + co ** 2))
hipotenusa_raiz = math.sqrt(hipotenusa)

print(f'\n\nO valor da hipotenusa é: {hipotenusa_raiz}')
