print('Responda o questionário a seguir para descobrir se você preenche todos os requisitos para servir ao Exército.\n')

idade = int(input('Insira a sua idade: '))
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))

# print(type(idade), type(peso), type(altura))

if(idade >= 18 and peso >= 60 and altura >= 1.70):
    print('\nParabéns! Você está apto a servir ao Exército.')
else:
    print('\nDesculpe, infelizmente você não preenche todos os requisitos necessários.')
