#import
from Acoes import Terminal
from Acoes import Menu
from Acoes import Funcoes

# Main Menu
while True:
    Terminal.titulo()
    Terminal.msg_entrada(['Olá, Tudo bem?','Me chamo Herik','sou o assistente virtual do Banco Herik','Estou aqui para te ajudar!','Aqui está um menu do que pode ser feito no nosso sistema:'],Terminal.titulo)
    Terminal.msg_entrada(['O que deseja fazer?'],Menu.menuzinho)
    opcao = input(' ')
    concluir_menu = Menu.menu(opcao)
    if not concluir_menu:
        continue
    else:
        break