import sqlite3
import os
from Classes import Aluno_Professor
from datetime import date
from time import sleep

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
            print('Equipamento Cadastrado com Sucesso!')
            conf = "N"

def reserva():
    os.system('cls') or None
    # conf = 'S'
    # while conf == "S":
    #Variável para buscar o CPF
    cpf = input('Digite o número do CPF: ')
    
    #Retorna Nome e Matricula do usuário
    try:
        numMatricula = listar_cadastro(cpf)[0]
        nomUser = listar_cadastro(cpf)[1]
        os.system('cls') or None
        print(f"Matrícula: {numMatricula}")
        print(f"Nome: {nomUser}")
        equipamento = input('Digite uma palavra chave do equipamento: ')
        idEquipamento = listar_equipamento(equipamento)[0]
        nomEquipamento = listar_equipamento(equipamento)[1]
        print(f"Número de série: {idEquipamento}")
        print(f"Equipamento: {nomEquipamento}")
        datReserva = input('Digite a data de reserva [yyyy-mm-dd]: ') 

        slv = input('Deseja Salvar a Reserva [S/N]? ')

        if  slv == "S" or slv == "s":
            #Abrindo conexão com o BD para persistir ou consultar dados
            conn = sqlite3.connect('SRE.db')
            cursor = conn.cursor()
            
            cursor.execute("""INSERT INTO TF_COMODATO (matAluno_Professor,idEquipamento,dtReserva,criado_em,idDevolvido)
                              VALUES (?,?,?,?,?,?,?)""",(numMatricula,idEquipamento,datReserva,date.today(),0))
            #Comita o comando
            conn.commit()
            #Fecha instancia com o BD
            conn.close()
            sleep(2)
            print('Reserva Cadastrada com  Sucesso!')
           
    except:
        print("Usuário ou Equipamento Não Encontrado!")
        sleep(2)
        os.system('cls') or None
            
def listar_cadastro(cpf):
    #Abrindo conexão com o BD para persistir ou consultar dados
    conn = sqlite3.connect('SRE.db')
    cursor = conn.cursor()
    
    #Busca o usuário
    query = "SELECT * FROM TD_CADASTRO WHERE CPF = '" + cpf + "'"
    cursor.execute(query)
    
    for linha in cursor.fetchall():
        nome = linha[2]
        matricula = linha[1]
    #Fecha a conexão
    conn.close()
    return matricula,nome


def listar_equipamento(equipamento):
    #Abrindo conexão com o BD para persistir ou consultar dados
    conn = sqlite3.connect('SRE.db')
    cursor = conn.cursor()
    
    #Busca o usuário
    query = "SELECT * FROM TD_EQUIPAMENTO WHERE desDescricao LIKE '%" + equipamento + "%'"
    cursor.execute(query)
    
    for linha in cursor.fetchall():
        descricao = linha[2]
        idEquipamento = linha[0]
    #Fecha a conexão
    conn.close()
    return idEquipamento,descricao











