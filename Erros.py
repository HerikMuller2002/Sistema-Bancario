import os
import time

def limpar():
    os.system('cls')

def congelar(tempo):
    time.sleep(tempo)

def error(erro):
    if erro == 'confirm':
        limpar()
        print('Erro!\nEmail e senha errado!')
        congelar(2)
        limpar()
        print('Tente novamente...')
        congelar(1)
    elif erro == 'TypeError':
        limpar()
        print('Erro!\nDigite um valor válido!')
        congelar(2)
        limpar()
        print('Tente novamente...')
        congelar(1)
    elif erro == 'invalid saque':
        limpar()
        print('Erro!\nSaque inválido!')
        congelar(2)
        limpar()
        print('Tente novamente...')
        congelar(1)
    