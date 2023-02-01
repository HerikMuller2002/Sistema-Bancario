from Cliente import CriarCliente
from Cliente import ExcluirCliente
from Erros import error
from Erros import congelar
from Erros import limpar
import json
import os

def titulo():
    limpar()
    print('{:=^50}\n'.format(' Banco Herik '))

def msg_entrada(texto,funcao=limpar):
    if type(texto) == str:
        msg = [texto]
    else:
        msg = texto
    for i in msg:
        lista = []
        congelar(1.5)
        funcao()
        for j in i:
            funcao()
            lista.append(j)
            tela = ''.join(lista)
            print(tela)
            congelar(0.06)

def carregando():
    limpar()
    for i in range(2):
        carregando = 'verificando.'
        for j in range(3):
            limpar()
            print(carregando)
            carregando += '.'
            congelar(0.5)

def entrada():
    titulo()
    msg_entrada(['Olá, Tudo bem?','Me chamo Herik','sou o assistente virtual do Banco Herik','Estou aqui para te ajudar!'],titulo)
    congelar(0.5)
    while True:
        titulo()
        msg_entrada(['O que deseja fazer?'],titulo)
        print()
        print('[1] Fazer login\n[2] Criar uma conta\n[3] Sobre nós\n')
        validas = ['1','2','3']
        opcao = input(' :')
        if opcao not in validas:
            error('TypeError')
        else:
            continuar = opcao_entrada(opcao)
            if not continuar:
                continue
            else:
                break

def input_dados(tipo_dados):
    if tipo_dados == 'criar':
        print('preecha as informações da conta:')
        nome = input('Nome: ')
        sobrenome = input('sobrenome: ')
        cpf = input('cpf: ')
        email = input('email: ')
        senha = input('senha: ')
        return nome,sobrenome,cpf,email,senha
    else:
        print('preecha as informações da conta:')
        email = input('email: ')
        senha = input('senha: ')
        return email,senha

def opcao_entrada(opcao):
    if opcao == '1':
        tentativas = 0
        while True:
            if tentativas < 3:
                validar,conta = login()
                if validar:
                    ContaCliente(conta)
                else:
                    error('confirm')
                    tentativas += 1
            else:
                return False
    elif opcao == '2':
        criar_conta()
        return False
    elif opcao == '3':
        sobre_nos()
        return False

def criar_conta():
    while True:
        opcao = input('Deseja criar uma conta?\n[s]im [n]ão: ')
        if opcao == 's':
            while True:
                nome,sobrenome,cpf,email,senha = input_dados('criar')
                confirm_email = input('confirme seu email: ')
                confirm_senha = input('confirme sua senha: ')
                if confirm_email != email or confirm_senha != senha:
                    error('confirm')
                    continue
                else:
                    cliente = CriarCliente(nome,sobrenome,cpf,email,senha,saldo=0)
                break
        else:
            break

def login():
    email,senha = input_dados('login')
    with open('data_base.json','r') as db:
        if os.stat('data_base.json').st_size == 0: # se o arquivo está vazio
            return False
        else: # se o arquivo não estiver vazio
            dados_cliente = json.load(db) # carregando a lista do arquivo
            for i in range(0,len(dados_cliente)):
                if dados_cliente[i]['senha'] == senha and dados_cliente[i]['email'] == email:
                    conta = dados_cliente[i]
                    return True,conta
                else:
                    return False

def sobre_nos():
    limpar()
    msg_entrada('Seção em desenvolvimento!')
    congelar(1.5)



class ContaCliente:

    def __init__(self,conta):
        self.conta = conta
        ContaCliente.menu_conta(self)

    def menu_conta(self):
        msg_entrada(['Aqui está algumas opções da sua conta!','O que deseja fazer?'])
        print('[1] Sacar\n[2] depositar\n[3]Ver saldo')
        opcao = input(' :')
        if opcao == '1':
            self.sacar()
        elif opcao == '2':
            self.depositar()
        else:
            self.ver_saldo()

    def sacar(self):
        saldo = self.saldo()
        while True:
            msg_entrada("Seu saldo é de R${:.2f}\n".format(saldo))
            print()
            msg_entrada('Quanto deseja sacar?')
            print()
            try:
                saque = float(input(" R$"))
                if saque < 0:
                    error("invalid saque")
                    continue
                else:
                    novo_saldo = saldo - saque
                    break
            except:
                error("invalid saque")
                continue
        return novo_saldo


    def depositar(self):
        ...
    
    def ver_saldo(self):
        saldo = self.saldo()
        msg_entrada('Seu saldo é de R${:.2f}'.format(saldo))

    def saldo(self):
        dados = self.conta
        saldo = dados['saldo']
        return saldo


    def excluir_conta(self):
        while True:
            opcao = input('Deseja excluir uma conta?\n[s]im [n]ão: ')
            if opcao == 's':
                while True:
                    email,senha = input_dados('excluir')
                    confirm_email = input('confirme seu email: ')
                    confirm_senha = input('confirme sua senha: ')
                    if confirm_email != email or confirm_senha != senha:
                        error('confirm')
                        continue
                    else:
                        del_cliente = ExcluirCliente(email,senha)
                        break
            else:
                break