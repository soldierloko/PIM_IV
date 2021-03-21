import sqlite3
import os
from Classes import Aluno_Professor

#Define o Menu Iniciar do Programa
def exibir_menu(): 
        # Cria o Menu Inicial
        print('*'*50)
        print(' '*24 + 'SRE')
        print('''

        1 - Cadastro
        2 - Reserva
        3 - Devolução
        4 - Relatório
        5 - Sair
        ''')
        print('*'*50)

def Abre_Banco():
    #Abrindo conexão com o BD para persistir ou consultar dados
    conn = sqlite3.connect('SRE.db')
    cursor = conn.cursor()

def Fecha_Banco():
    #Fecha instancia com o BD
    conn.close()

#Função de novos cadastros
def cadastro():
    os.system('cls') or None

    conf = "S"
    while conf == "S":
        a = Aluno_Professor(AP = input('Digite a [P] para Professor e [A] para Aluno: ').upper
                            ,matricula = input('Digite a Matricula: ').upper
                            ,nome = input('Digite o Nome: ').upper
                            ,cpf = input('Digite o CPF: ').upper
                            ,email = input('Digite o Email: ').upper
                            ,telefone = input('Digite o Telefone: ').upper
                            ,dtNasc = input('Digite a Data de Nascimento: ').upper)

        print(f"A = Aluno / P = Professor: {a.AP()}")
        print(f"Matricula: {a.matricula()}")
        print(f"Nome: {a.nome()}")
        print(f"CPF: {a.cpf()}")
        print(f"E-mail: {a.email()}")
        print(f"Telefone: {a.telefone()}")
        print(f"Data de Nascimento: {a.dtNasc()}")
        Ins = input('Deseja Salvar o Cadastro [S/N]? ')

        if Ins.upper == 'S':
            Abre_Banco()
            cursor.execute("INSERT INTO TD_CADASTRO VALUES ('" + a.AP() + "','" + a.matricula() + "','" + a.nome() + "','" + a.cpf() + "','" + a.email() + "','" + a.telefone() + "','" + a.dtNasc() + "')")
            conn.commit()
            Fecha_Banco()
            exibir_menu()





















def listar(pessoas):
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        print(f'Nome: {nome}, idade: {idade}, id: {identificador}')

def buscar(pessoas):
    identificador_desejado = input('Id? ')
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        if identificador == identificador_desejado:
            print(f'Nome: {nome}, idade: {idade}, id: {identificador}')
            break
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')

