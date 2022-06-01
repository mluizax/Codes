# n = (n-1) + (n-2)

seq_size = int(input("Quantidade de números para a sequência: "))

number_one, number_two = 1, 1
count = 0  # posição

if seq_size <= 0:
    print("Escolha um número positivo e maior que zero.")
elif seq_size == 1:
    print("Não pode ter somente um número na sequência, você inseriu", seq_size, ":")
    print(number_one)
else:
    print("Fibonacci para a sequência escolhida:")
    while count < seq_size:
        print(number_one)
        nth = number_one + number_two
        number_one = number_two
        number_two = nth
        count += 1
