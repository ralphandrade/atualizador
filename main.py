# lista de  nomes
nomes = ['Ralph', 'Julia', 'Carlos', 'Carla', 'Joana', 'José']

# usuário informa o índice que deseja alterar
indice = int(input('Informe o índice que deseja alterar: '))
indice -= 1

# usuário informa o novo nome
nomes[indice] = input('Informe o novo nome: ')

# exibe a lista
for nome in nomes:
    print(nome)