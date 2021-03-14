from datetime import date as dt
class Pessoa:
    def __init__(self, nome, cpf, email, telefone, dtNasc):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.dtNasc = dtNasc
        self.classificacao = classificacao 
    
    def setNome(self,nome):
        self.nome = nome

    def getNome(self,nome):
        return self.nome

class Usuario(Pessoa):
    def __init__(self,)