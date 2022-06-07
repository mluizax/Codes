print('\tSeja bem-vindo(a) ao controle de festas da Maria Luíza!\n')

quantidade = int(input('Quantas pessoas serão convidadas para a festa? '))
aux = 0
list = []

while aux < quantidade:
    convidado = str(input(f'Nome do convidado número {aux+1}: '))
    list.append(convidado)
    aux += 1

print('\nLista com todos os convidados: ')
for convidado in list:
    print(convidado)
