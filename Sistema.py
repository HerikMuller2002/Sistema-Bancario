from Cliente import CriarCliente
from Cliente import ExcluirCliente
import json
import os
import time

###################################################

def limpar():
    os.system('cls')

def congelar(tempo):
    time.sleep(tempo)

def error(erro):
    if erro == 'confirm':
        limpar()
        titulo()
        print('Erro!\nEmail e senha errados!')
        congelar(2)
        limpar()
        titulo()
        print('Tente novamente...')
        congelar(1)
    elif erro == 'TypeError':
        limpar()
        titulo()
        print('Erro!\nDigite um valor válido!')
        congelar(2)
        limpar()
        titulo()
        print('Tente novamente...')
        congelar(1)
    elif erro == 'invalid saque':
        limpar()
        titulo()
        print('Erro!\nSaque inválido!')
        congelar(2)
        limpar()
        titulo()
        print('Tente novamente...')
        congelar(1)
    elif erro == 'invalid deposito':
        limpar()
        titulo()
        print('Erro!\nDeposito inválido!')
        congelar(2)
        limpar()
        titulo()
        print('Tente novamente...')
        congelar(1)
    elif erro == 'opcao':
        limpar()
        titulo()
        print('Erro!\nOpção inválida!')
        congelar(2)
        limpar()
        titulo()
        print('Tente novamente...')
        congelar(1)

###################################################   

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
    for i in range(0,3):
        carregando = 'Carregando.'
        for j in range(3):
            limpar()
            titulo()
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
        msg_entrada('preecha as informações da conta:',titulo)
        print()
        nome = input('Nome: ')
        sobrenome = input('sobrenome: ')
        cpf = input('cpf: ')
        email = input('email: ')
        senha = input('senha: ')
        return nome,sobrenome,cpf,email,senha
    else:
        msg_entrada('preecha as informações da conta:',titulo)
        print()
        email = input('email: ')
        senha = input('senha: ')
        return email,senha

###################################################   

def opcao_entrada(opcao):
    if opcao == '1':
        tentativas = 0
        while True:
            if tentativas < 3:
                validar,conta = login()
                if validar:
                    ContaCliente(conta)
                    return False
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
    carregando()
    while True:
        limpar()
        titulo()
        opcao = input('Deseja criar uma conta?\n[s]im [n]ão: ').lower()
        if opcao == 's':
            while True:
                limpar()
                titulo()
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
    carregando()
    email,senha = input_dados('login')
    with open('data_base.json','r') as db:
        if os.stat('data_base.json').st_size == 0: # se o arquivo está vazio
            return False,None
        else: # se o arquivo não estiver vazio
            dados_cliente = json.load(db) # carregando a lista do arquivo
            i = 0
            while i < len(dados_cliente):
                if dados_cliente[i]['senha'] == senha and dados_cliente[i]['email'] == email:
                    conta = dados_cliente[i]
                    return True,conta
                else:
                    i += 1
            return False

def sobre_nos():
    carregando()
    limpar()
    msg_entrada('Seção em desenvolvimento!',titulo)
    congelar(1.5)


######################################################################
# Classe conta do cliente
######################################################################

class ContaCliente: # classe cliente

    def __init__(self,conta_selecionada): # função para criar o objeto conta
        self.conta_selecionada = conta_selecionada # definido a variável para o objeto conta
        with open('data_base.json','r',encoding='utf-8') as db: # abrindo o arquivo em modo escrita
            self.dados = json.load(db) # método dump para escrever a lista no json
        i = 0
        while i < len(self.dados):
            if self.dados[i]['email'] == self.conta_selecionada['email']:
                self.conta = self.dados[i]
                break
            else:
                i += 1
        self.menu_conta() # chamando a função 'menu_conta', para mostar o menu das opções

    def menu_conta(self): # função para mostrar o menu das ações na conta
        while True:
            carregando()
            msg_entrada(['Aqui está algumas opções da sua conta!','O que deseja fazer?'],titulo)
            print('\n[1] Sacar\n[2] depositar\n[3] Ver saldo\n[4] Excluir conta\n[5] Sair\n')
            opcao = input(' :')
            validos = ['1','2','3','4','5']
            if opcao not in validos:
                error('opcao')
            else:
                if opcao == '1':
                    self.sacar()
                elif opcao == '2':
                    self.depositar()
                elif opcao == '3':
                    self.ver_saldo()
                elif opcao == '4':
                    excluiu = self.excluir_conta()
                    if excluiu:
                        break
                else:
                    break

    def sacar(self):
        carregando()
        saldo = self.saldo()
        while True:
            msg_entrada("Seu saldo é de R${:.2f}\n".format(saldo),titulo)
            print()
            msg_entrada('Quanto deseja sacar?',titulo)
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
        self.new_saldo(novo_saldo)


    def depositar(self):
        carregando()
        saldo = self.saldo()
        while True:
            msg_entrada("Seu saldo é de R${:.2f}\n".format(saldo))
            print()
            msg_entrada('Quanto deseja depositar?')
            print()
            try:
                deposito = float(input(" R$"))
                if deposito < 0:
                    error("invalid deposito")
                    continue
                else:
                    novo_saldo = saldo + deposito
                    break
            except:
                error("invalid deposito")
                continue
        self.new_saldo(novo_saldo)
    
    def ver_saldo(self):
        carregando()
        saldo = self.saldo()
        msg_entrada('Seu saldo é de R${:.2f}'.format(saldo),titulo)
        return False

    def saldo(self):
        dados = self.conta
        saldo = dados['saldo']
        return saldo
    
    def new_saldo(self,novo_saldo):
        conta = self.conta
        dados = self.dados
        i = 0
        while i < len(dados):
            if dados[i]['senha'] == conta['senha']:
                dados[i]['saldo'] = novo_saldo
                break
            else:
                i += 1
        with open('data_base.json','w',encoding='utf-8') as db: # abrindo o arquivo em modo escrita
            json.dump(dados, db) # método dump para escrever a lista no json

    def excluir_conta(self):
        carregando()
        while True:
            limpar()
            titulo()
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
                        excluiu = ExcluirCliente(email,senha)
                        return excluiu
            else:
                break