#Importa as Bibliotecas necessárias
import sqlite3
import pandas as pd
import os 
from time import sleep
from Classes import Pessoa

#Abrindo conexão com o BD para persistir ou consultar dados
conn = sqlite3.connect('SRE.db')

# Verifica a entrada de dados do usuário, enquanto não for de 1 a 5 ele não sai do loop
while True:
    # Verifica se o usuário esta digitando números
    try:
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

        #Entrada de escolha do usuário
        n = int(input('Escolha uma opção:')) 
        #Verifica se o usuário digitou as opções corretas     
        if  n == 1 :
            os.system('cls') or None
            while True:

                try:

                    # Cria o Menu Secundário
                    print('*'*50)
                    print(' '*24 + 'Cadastro')
                    print('''

                    1 - Novo Cliente
                    2 - Novo Usuário
                    3 - Consulta
                    4 - Voltar
                    ''')
                    print('*'*50)

                    op = int(input('Digite uma das opções acima: '))
                    if op ==1:
                        os.system('cls') or None
                        nome = input('Digite o Nome: ')
                        cpf = input('Digite o CPF: ')
                        mail = input('Digite o Email: ')
                        telefone = input('Digite o Telefone: ')
                        dtNascimento = input('Digite a Data de Nascimento: ')
                        classificacao = 1

                        Pessoa(nome,cpf,email,telefone,dtNascimento,classificacao)
                        print(Pessoa)
                        break                        
                        # a Data de Corte [DD/MM/AAAA]
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    elif op ==2:
                        dt_ex = input('Digite a Data de Corte [DD/MM/AAAA]: ')
                        FN.del_registro(dt_ex,2)
                        FN.Int_Grafica(7)
                        break
                    elif op ==3:
                        os.system("cls") or None
                        break
                    else:
                        print('Opção Invalida!') 
                        sleep(2)
                        os.system("cls") or None

                except:
                    print('Opção Invalida!') 
                    sleep(2)
                    os.system("cls") or None
        
        elif n == 2:
            print('Teste')

        elif n == 3:
            print('Teste')

        elif n == 4:
            print('Teste')

        elif n == 5:
            print('Saindo do sistema!')
            #Fecha instancia com o BD
            conn.close()
            sleep(2)
            #Para o Loop
            break
        #Retorna Opção inválida
        else:
            print('Entrada Invalida!')
            sleep(2)
            os.system("cls") or None
    except:
        print('Opção Invalida!') 
        sleep(2)
        os.system("cls") or None
