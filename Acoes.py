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
    
    def menuzinho():
        Terminal.titulo()
        print('[1] Fazer login\n[2] Criar uma conta\n[3] Sobre nós\n')


    def menu(opcao):
        try:
            if opcao == 1:
                Terminal.msg_entrada(['Entre com seu email e senha, caso não tenha... crie uma conta!'],Terminal.titulo)
                email = input('Email: ')
                senha = input('Senha: ')
                Funcoes.verificar(email,senha)
        except:
            ...

class Funcoes:
    ...