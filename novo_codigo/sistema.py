from classes import Client


lista = []
while True:
    adicionar = input('Deseja adicionar um usuário?\n[s]im [n]ão: ')
    if adicionar == 's':
        nome = input('Nome: ')
        email = input('email: ')
        senha = input('senha: ')
        cliente = Client(nome,email,senha)
    else:
        break