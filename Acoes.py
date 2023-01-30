# import
import os
import time

class Terminal:

    def limpar_terminal():
        os.system('cls')
    
    def congelar(tempo):
        time.sleep(tempo)

    def titulo():
        Terminal.limpar_terminal()
        print('{:=^50}\n'.format(' Banco Herik '))
    
    def msg_entrada(msg,funcao):
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
        if opcao == '1':
            while True:
                Terminal.msg_entrada(['Entre com seu email e senha...\nCaso não tenha... crie uma conta!\n'],Terminal.titulo)
                email = input('Email: ')
                senha = input('Senha: ')
                print()
                Terminal.carregando()
                '''validacao = Funcoes.verificar(email,senha)
                if not validacao:
                    continue
                else:
                    break'''
        elif opcao == '2':
            ...
        elif opcao == '3':
            print('Esta seção ainda está sendo finalizada!')
            Terminal.congelar(2)
            return False


class Funcoes:
    ...