import json
import os

class CriarCliente: # Classe das informações do cliente

    def __init__(self,nome,sobrenome,cpf,email,senha,saldo): # função para carregar os atributos do cliente
        self.nome = nome # definindo o atributo 'nome'
        self.sobrenome = sobrenome # definindo o atributo 'sobrenome'
        self.cpf = cpf # definindo o atributo 'cpf'
        self.email = email # definindo o atributo 'email'
        self.senha = senha # definindo o atributo 'senha'
        self.saldo = saldo # definindo o atributo 'saldo'
        with open('data_base.json','r',encoding='utf-8') as db: # abrindo o arquivo json em modo leitura
            if os.stat('data_base.json').st_size == 0: # se o arquivo está vazio
                lista = [] # criando uma lista vazia para guardar os dicionários
            else: # se o arquivo não estiver vazio
                lista = json.load(db) # carregando a lista do arquivo     
        self.json(lista) # chamando a função json e passando o parâmetro "lista"
    
    def json(self,dados): # função para escrever a lista criada com os atributos, no arquivo json
        lista = self.dicionario(dados) # chamando a função dicionario e guardando a lista com os dicionários criados com os atributos, na variável 
        with open('data_base.json','w',encoding='utf-8') as db: # abrindo o arquivo em modo escrita
            json.dump(lista, db) # método dump para escrever a lista no json

    def dicionario(self,lista): # função para criar um dicionário com os atributos do cliente
        dados = {'nome':self.nome,'email':self.email,'senha':self.senha,'saldo':self.saldo} # criando o dicionário
        lista.append(dados) # guardando o dicionário em uma lista para guardar outros dicionários no futuro
        return lista # retornando a lista com o dicionário



class ExcluirCliente:

    def __init__(self,email,senha): # função para carregar os atributos do cliente
        self.email = email # definindo o atributo 'email'
        self.senha = senha # definindo o atributo 'senha'
        self.excluir(email,senha)
    
    def excluir(self,email,senha):
        with open('data_base.json','r',encoding='utf-8') as db: # abrindo o arquivo json em modo leitura
            lista = json.load(db) # carregando a lista do arquivo
            i = 0 
            while i < len(lista):
                if lista[i]['senha'] == senha and lista[i]['email'] == email:
                    lista.remove(lista[i])
                    with open('data_base.json','w',encoding='utf-8') as db: # abrindo o arquivo em modo escrita
                        json.dump(lista, db) # método dump para escrever a lista no json
                        break
                else:
                    i += 1
        return True