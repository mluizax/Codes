operacao = input("Digite a operação matemática desejada (soma, sub, mult, div): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

# input devolve uma string -> operação matemática usa variáveis numéricas
# converter string em valor numérico -> usa função str

if operacao == "soma":
    resultado = int(numero1) + int(numero2)
elif operacao == "sub":
    resultado = int(numero1) - int(numero2)
elif operacao == "mult":
    resultado = int(numero1) * int(numero2)
elif operacao == "div":
    resultado = int(numero1) / int(numero2)
else:
    resultado = "A operação não pode ser realizada"

# OBS.: em py usa elif para relacionar os if

print("O resultado da operação é: " + str(resultado))
