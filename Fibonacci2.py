# n = (n-1) + (n-2)

seq_size = int(input('Escolha o tamanho da sequência: '))

number_one, number_two = 1, 1
count = 0

if(seq_size <= 0):
    print('Por favor, escolha um número maior do que zero.')
elif(seq_size == 1):
    print('Tente novamente! A sua sequência precisa ter mais de um termo.')
while(count < seq_size):
    print(number_one)
    nth = number_one + number_two
    number_one = number_two
    number_two = nth
    count += 1
