# import
from Cliente import CriarCliente
from Cliente import ExcluirCliente
import json
import os
import time

######################################################################
# Funções de erros
######################################################################

def msg_erro(erro): # função para imprimir a mensagem de erro na tela
    limpar() # função para limpar o terminal
    titulo() # função para imprimir o título
    print('Erro!\n{}'.format(erro)) # imprimindo o erro na tela
    congelar(2) # função para congelar a tela
    limpar() # função para limpar o terminal
    titulo() # função para imprimir o título
    print('Tente novamente...') # imprimindo "tente novamente na tela"
    congelar(1) # função para congelar a tela

def error(erro): # função para definir o tipo de erro
    if erro == 'confirm': # erro de confirmação de senha
        msg_erro('Email e senha errados!') # chamando a função para imprimir a mensagem expecífica
       
    elif erro == 'TypeError': # erro de tipagem de entrada
        msg_erro('Digite um valor válido!') # chamando a função para imprimir a mensagem expecífica

    elif erro == 'invalid saque': # valor de saque inválido
        msg_erro('Saque inválido!')# chamando a função para imprimir a mensagem expecífica

    elif erro == 'invalid deposito': # valor de depósito inválido
        msg_erro('Deposito inválido!') # chamando a função para imprimir a mensagem expecífica

    elif erro == 'opcao':
        print('Erro!\nOpção inválida!') # opção inválida
        msg_erro('Opção inválida!') # chamando a função para imprimir a mensagem expecífica

######################################################################
# Funções de 'Terminal', para imprimir ou apagar informações no terminal
###################################################################### 

def limpar(): # função para limapar o terminal
    os.system('cls') # chamando o método system para imprimir o comando 'cls' no terminal

def congelar(tempo): # função para congelar a tela por alguns segundos
    time.sleep(tempo) # chamando o método 'sleep' para congelar o terminal par alguns segundos

def titulo(): # função para imprimir o nome do sistema 'banco herik'
    limpar() # chamando a função limpar, para limpar o terminal
    print('{:=^50}\n'.format(' Banco Herik ')) # imprimindo o nome do sistema 'banco herik' na tela

def msg_entrada(texto,funcao=limpar): # função para imprimir texto na tela com animação do 'assistente virtual'
    if type(texto) == str: # verificando se o tipo do parâmetro é string
        msg = [texto] # guardando a string em uma lista
    else: # se o parâmetro já for uma lista... 
        msg = texto # armazenando a lista na varível utilizada na função
    for i in msg: # loop para limpar a frase impressa na tela e começar uma nova frase
        lista = [] # criando uma nova lista para guardar letra por letra que será impressa na tela
        congelar(1.5) # chamando a função congelar, para congelar a frase na tela, dando tempo para o usuário ler 
        funcao() # antes de imprimir algum texto na tela, é executado uma função para fins estéticos. como as funções limpar(),titulo()...
        for j in i: # loop para imprimir letra por letra, dando a sensação de animação
            funcao() # antes de imprimir algum texto na tela, é executado uma função para fins estéticos. como as funções limpar(),titulo()...
            lista.append(j) # adicionando a letra em uma nova lista para que ela seja mostrada junto com as que virão, dando a sensação de animação de digitação no terminal
            tela = ''.join(lista) # transformando a nova lista em string para imprimir na tela
            print(tela) # imprimindo a nova lista na tela
            congelar(0.06) # congelando a tela por alguns milésimos para dar a sensação de animação

def carregando(): # função para imprimir carregando na tela, para dar a sensção de um sistema dinâmico com requisições
    for i in range(0,3): # loop para definir uma variável de controle
        carregando = 'Carregando.' # definindo a string com apenas um '.'
        for j in range(3): # loop de controle
            limpar() # função para limpar o terminal
            titulo() # função para imprimir o nome do sistema no terminal
            print(carregando) # imprimindo a string 'carregando' na tela
            carregando += '.' # concatenando um '.' na string para dar a sensação de animação, devido a variação de '.' com o loop
            congelar(0.5) # congelando a tela por alguns milésimos para que o usuário veja as transições de '.', dando a sensação de animação

def inicio(): # função para iniciar o sistema
    titulo() # função para imprimir o nome do sistema na tela
    msg_entrada(['Olá, Tudo bem?','Me chamo Herik','sou o assistente virtual do Banco Herik','Estou aqui para te ajudar!'],titulo) # função para imprimir uma string na tela como 'animação'
    congelar(0.5) # congelando a tela 
    while True: # loop 
        titulo() # função para mostrar o nome do sistema na tela
        msg_entrada(['O que deseja fazer?'],titulo) # função para imprimir uma string na tela como 'animação'
        print() # imprimindo um espaço vazio para separar as linhas
        print('[1] Fazer login\n[2] Criar uma conta\n[3] Sobre nós\n') # imprimindo as opções do menu principal do sistema
        validas = ['1','2','3'] # criando uma lista de inputs válidos
        opcao = input(' :') # input da opção escolhida pelo usuário
        if opcao not in validas: # verificando se opção é válida
            error('TypeError') # função para imprimir mensagem de erro 
        else: # se a opção escolhida pelo usuário for válida, continuamos o programa
            continuar = opcao_entrada(opcao) # chamando a função 'opcao_entrada' para verificar qual foi a opção escolhida pelo usuário e guardando o retorno booleando da função em uma variável de controle
            if not continuar: # se a variável for False, continuamos o loop para perguntar novamente ao usuário 
                continue # continuando o loop
            else: # se a variável for True, paramos o loop e continuamos o sistema
                break # parando o loop

def input_dados(tipo_dados): # função para input das informações do usuário
    if tipo_dados == 'criar': # verificando qual vai ser o tipo de input para pedir ao usuário
        msg_entrada('preecha as informações da conta:',titulo) # função para imprimir uma string na tela como 'animação'
        print() # imprimindo um separador de linhas
        nome = input('Nome: ') # input do nome do usuário
        sobrenome = input('sobrenome: ') # input do sobrenome do usuário
        cpf = input('cpf: ') # input do cpf do usuário
        email = input('email: ') # input do email do usuário
        senha = input('senha: ') # input do senha do usuário
        return nome,sobrenome,cpf,email,senha # retornado os inputs
    else: # verificando qual vai ser o tipo de input para pedir ao usuário
        msg_entrada('preecha as informações da conta:',titulo) # função para imprimir uma string na tela como 'animação'
        print() # imprimindo um separador de linhas
        email = input('email: ') # input do email do usuário
        senha = input('senha: ') # input da senha do usuário
        return email,senha # retornando os inputs

######################################################################
# Funções do menu principal
######################################################################  

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
            return False,None

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