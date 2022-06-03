pessoas = list()

ok = True
while ok:

    # Menu Inicio
    print('Seja bem-vindo ao registro de usuários.\n')
    print('[1] - Realizar um cadastro\n')
    print('[2] - Cancelar um cadastro\n')
    print('[3] - Listar os usuários cadastrados\n')
    print('[4] - Idade média dos usuários cadastrados\n')
    print('[0] - Sair do programa\n')

    menuop = input('Digite o número da opção desejada: ')

# Fecha programa
    if menuop == '0':
        ok = False

# Menu pessoa
    elif menuop == '1':
        nome = input('Informe o nome: ')
        cpf = input('Informe o CPF: ')
        idade = input('Informe a idade: ')

        pessoa = {}

        pessoa['nome'] = nome

        pessoa['cpf'] = cpf

        pessoa['idade'] = idade

        pessoas.append(pessoa)

# 4 Remover uma pessoa
    elif menuop == '2':
        consultar = input('\nInforme o CPF do usuário que deseja remover: ')
        for i, p in enumerate(pessoas):
            # print(p, i) -> verificando
            if(p['cpf']) == consultar:
                del pessoas[i]
                print(f'CPF {i} removido com sucesso.')
            else:
                print('CPF inexistente.')

# 5 Imprimir lista
    elif menuop == '3':
        print('Lista com todos os usuários do sistema: \n')
        for p in pessoas:
            print(p)

    elif menuop == '4':
        print('A idade média dos usuários cadastrados é: ')
        sum = 0
        for p in pessoas:
            sum += int(p['idade'])
        print(sum/len(pessoas))

print('Finalizando o programa...')
