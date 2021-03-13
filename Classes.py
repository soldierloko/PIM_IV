from datetime import date as dt
class Pessoa:
    def __init__(self, nome, cpf, email, telefone, dtNasc,classificacao,dtcadastro = dt.today()):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.dtNasc = dtNasc
        self.classificacao = classificacao 
        self.dtcadastro = dtcadastro
    pass

