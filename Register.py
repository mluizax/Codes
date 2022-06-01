# Registro: salvar o nome e a idade do usuário em um dicionário
# e posteriormente enviar para uma lista

n = 2  # número de vezes que vai rodar e solicitar nome + idade

people = []

for number in range(n):
    person = {}

    name = input('Insira o seu nome: ')

    age = input('Insira a sua idade: ')

    person[name] = age

    people.append(person)

print(people)
