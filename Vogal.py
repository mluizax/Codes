v = ['a', 'e', 'i', 'o', 'u']


def verifique_se_e_vogal():
    letter = input('Escolha a letra para verificar se é vogal: ')
    if letter in v:
        print('É vogal!')
    else:
        print('Não é vogal.')


verifique_se_e_vogal()
