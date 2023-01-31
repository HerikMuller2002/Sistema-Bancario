# import
import os
import time
import json
import sys

class Terminal:

    def limpar_terminal():
        os.system('cls')
    
    def congelar(tempo):
        time.sleep(tempo)

    def titulo():
        Terminal.limpar_terminal()
        print('{:=^50}\n'.format(' Banco Herik '))
    
    def msg_entrada(msg,funcao=None):
        for i in msg:
            lista = []
            Terminal.congelar(1.5)
            funcao()
            for j in i:
                funcao()
                lista.append(j)
                tela = ''.join(lista)
                print(tela)
                Terminal.congelar(0.06)
    
    def carregando():
        Terminal.limpar_terminal()
        for i in range(2):
            carregando = 'verificando.'
            for j in range(3):
                Terminal.limpar_terminal()
                print(carregando)
                carregando += '.'
                time.sleep(0.5)
                
class Menu:
    
    def menuzinho():
        Terminal.titulo()
        print('[1] Fazer login\n[2] Criar uma conta\n[3] Sobre nós\n')

    def menu(opcao):
        while True:
            if opcao == '1':
                while True:
                    Terminal.msg_entrada(['Entre com seu email e senha...\nCaso não tenha... crie uma conta!'],Terminal.titulo)
                    print('[1] Criar conta\n')
                    email = input('Email: ')
                    senha = input('Senha: ')
                    Terminal.carregando()
                    validacao = Funcoes.verificar(email,senha)
                    if not validacao:
                        Terminal.limpar_terminal()
                        print("Ops... Ocorreu um erro!")
                        Terminal.congelar(2)
                        Terminal.limpar_terminal()
                        print("Tente novamente!")
                        Terminal.congelar(2)
                        Terminal.limpar_terminal()
                        continue
                    else:
                        break
            elif opcao == '2':
                Funcoes.criar()
                return False
            elif opcao == '3':
                Terminal.msg_entrada(['Esta seção ainda está sendo finalizada!'],Terminal.limpar_terminal)
                Terminal.congelar(1)
                return False

class Funcoes:
    
    def criar():
        while True:
            Terminal.msg_entrada(['Preencha as informações a seguir:'],Terminal.limpar_terminal)
            print()
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            cpf = input('CPF: ')
            email = input('Email: ')
            while True:
                senha = input('Senha: ')
                confirma_senha = input('Confirme sua senha: ')
                if confirma_senha != senha:
                    Terminal.limpar_terminal()
                    print('Ops... senha incorreta!')
                    Terminal.congelar(2)
                    continue
                else:
                    break                    
            Terminal.limpar_terminal()
            Terminal.msg_entrada(['Continuar [s]im  [n]ão :'],Terminal.limpar_terminal)
            continuar = input(' ').lower()
            if continuar == 's':
                user = {'nome':nome,'sobrenome':sobrenome,'cpf':cpf,'email':email,'senha':senha}
                with open('data_base.json','w',encoding='utf-8') as db:
                    json.dump(user,db)
                break
            else:
                continue

    def verificar(email, senha):
        with open('data_base.json','r') as db:
            dados = json.load(db)
            print(dados)
            sys.exit()