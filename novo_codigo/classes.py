import json

class Client:

    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        with open('data_base.json','r',encoding='utf-8') as db:
            lista = json.load(db)
            print(lista)           
        self.json(lista)
    
    def dicionario(self,lista):
        dados = {'nome':self.nome,'email':self.email,'senha':self.senha}
        lista.append(dados)
        return lista
    
    def json(self,dados):
        lista = self.dicionario(dados)
        with open('data_base.json','w',encoding='utf-8') as db:
            json.dump(lista, db)