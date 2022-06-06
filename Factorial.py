number = int(input('Insira um número para calcular o seu fatorial: '))


def factorial(number):
    if number < 0:
        print("Operação não suportada com número negativo.")

    elif number == 0:
        return 1

    else:
        aux = 1
        while(number > 1):
            aux *= number
            number -= 1
        return aux


print(f'O fatorial de {number} é {factorial(number)}.')
