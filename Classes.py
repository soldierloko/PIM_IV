class Pessoa:
    def __init__(self, matricula, nome, cpf, email, telefone, dtNasc):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.dtNasc = dtNasc

    def setNome(self,matricula):
        self.matricula = matricula

    def setNome(self,nome):
        self.nome = nome

    def setNome(self,cpf):
        self.cpf = cpf

    def setNome(self,email):
        self.email = email

    def setNome(self,telefone):
        self.telefone = telefone

    def setNome(self,dtNasc):
        self.dtNasc = dtNasc

    def getMatricula(self):
        return self.matricula

    def getNome(self):
        return self.nome

    def getNome(self):
        return self.cpf

    def getNome(self):
        return self.email

    def getNome(self):
        return self.telefone

    def getNome(self):
        return self.dtNasc

class Aluno_Professor(Pessoa):
    def __init__(self, AP, matricula,nome, cpf, email, telefone, dtNasc):
        super().__init__(matricula, nome, cpf, email, telefone, dtNasc)
        self.AP = AP

    def setAP(self,AP):
        self.AP = AP

    def getAP(self):
        return self.AP




