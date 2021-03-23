import sqlite3
import os
from Classes import Aluno_Professor
from datetime import date
from datetime import sleep

#Define o Menu Iniciar do Programa
def exibir_menu(): 
        # Cria o Menu Inicial
        print('*'*50)
        print(' '*24 + 'SRE')
        print('''

        1 - Cadastro
        2 - Cadastro Equipamento
        3 - Reserva
        4 - Devolução
        5 - Relatório
        6 - Sair
        ''')
        print('*'*50)

#Função de novos cadastros
def cadastro():
    os.system('cls') or None
    slv = "N"
    conf = "S"
    #Faça até que eu mande Sair
    while conf == "S":
        #Armazena os valores nas classes criadas
        a = Aluno_Professor(AP = input('Digite a [P] para Professor e [A] para Aluno: ').upper
                            ,matricula = input('Digite a Matricula: ').upper
                            ,nome = input('Digite o Nome: ').upper
                            ,cpf = input('Digite o CPF: ').upper
                            ,email = input('Digite o Email: ').lower
                            ,telefone = input('Digite o Telefone: ').upper
                            ,dtNasc = input('Digite a Data de Nascimento: ').upper)

        #Coloca na tela todos os valores armazenados
        print(f"A = Aluno / P = Professor: {a.AP()}")
        print(f"Matricula: {a.matricula()}")
        print(f"Nome: {a.nome()}")
        print(f"CPF: {a.cpf()}")
        print(f"E-mail: {a.email()}")
        print(f"Telefone: {a.telefone()}")
        print(f"Data de Nascimento: {a.dtNasc()}")
        #Pergunta se quer mesmo cadastrar o usuário
        slv = input('Deseja Salvar o Cadastro [S/N]? ')

        if  slv == "S" or slv == "s":
            #Abrindo conexão com o BD para persistir ou consultar dados
            conn = sqlite3.connect('SRE.db')
            cursor = conn.cursor()
            
            #Comando para inserir na Tabela de Usuários
            cursor.execute("""INSERT INTO TD_CADASTRO (Aluno_Professor,matricula,nome,cpf,email,fone,dtNascimento,criado_em)
                              VALUES (?,?,?,?,?,?,?,?)""",(a.AP(),a.matricula(),a.nome(),a.cpf(),a.email(),a.telefone(),a.dtNasc(),date.today()))
            #Comita o comando
            conn.commit()
            #Fecha instancia com o BD
            conn.close()
            sleep(2)
            print('Cadastro Realizado com Sucesso!')
            conf = "N"

#Função de novos Equipamentos
def equipamento():
    os.system('cls') or None
    slv = "N"
    conf = "S"
    while conf == "S":
        numSerie = input('Digite o número de série: ')
        desDescricao = input('Digite a descrição do Equipamento: ')
        dtCompra = input('Digite a data de compra [yyyy-mm-dd]: ')
        desTipo = input('Digite o tipo [Audio/Video/Apoio]: ')
        desMarca = input('Digite o Fabricante: ')

        slv = input('Deseja Salvar o Equipamento [S/N]? ')

        if  slv == "S" or slv == "s":
            #Abrindo conexão com o BD para persistir ou consultar dados
            conn = sqlite3.connect('SRE.db')
            cursor = conn.cursor()
            
            cursor.execute("""INSERT INTO TD_EQUIPAMENTO (numSerie,desDescricao,dtCompra,desTipo,desMarca,criado_em)
                              VALUES (?,?,?,?,?,?)""",(numSerie,desDescricao,dtCompra,desTipo,desMarca,date.today()))
            #Comita o comando
            conn.commit()
            #Fecha instancia com o BD
            conn.close()
            sleep(2)
            print('Equipamento Cadastrado Sucesso!')
            conf = "N"

# def reserva():
#     os.system('cls') or None
#     slv = "N"
#     conf = "S"
#     while conf == "S":
#         #Variável para buscar o CPF
#         numCpf = input('Digite o número do CPF: ')
        
#         #Abrindo conexão com o BD para persistir ou consultar dados
#         conn = sqlite3.connect('SRE.db')
#         cursor = conn.cursor()


#         if  slv == "S" or slv == "s":
#             #Abrindo conexão com o BD para persistir ou consultar dados
#             conn = sqlite3.connect('SRE.db')
#             cursor = conn.cursor()
            
#             #Busca o usuário
#             cursor.execute("SELECT * FROM TD_CADASTRO WHERE LIKE '" + numCpf + "'")
#             for linha in cursor.fetchall():
#             print(linha)
        
            
            
            
            
            
            
            # #Comita o comando
            # conn.commit()
            # #Fecha instancia com o BD
            # conn.close()
            # sleep(2)
            # print('Equipamento Cadastrado Sucesso!')
            # conf = "N"
    


def listar_cadastro(cpf):
    #Abrindo conexão com o BD para persistir ou consultar dados
    conn = sqlite3.connect('SRE.db')
    cursor = conn.cursor()
    
    #Busca o usuário
    cursor.execute("SELECT * FROM TD_CADASTRO WHERE CPF LIKE '" + numCpf + "'")
    try:
        for linha in cursor.fetchall():
            print(linha)
    except:
        print("Usuário Não encontrado")
    #Fecha instancia com o BD
    conn.close()
    return













