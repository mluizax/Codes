number = int(input('Digite um número entre 0 e 100 para descobrir se é ímpar: '))
rest = number % 2

if number in range(0, 101):
    if rest == 0:
        print(f'O número "{number}" não é ímpar.')
    else:
        print(f'O número "{number}" é ímpar.')
