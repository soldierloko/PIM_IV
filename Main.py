#Importa as Bibliotecas necessárias
import sqlite3
import pandas as pd
import os 
from time import sleep
import Classes as cl

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
            os.system('cls')
            print('Teste')
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
            os.system('cls')
    except:
        print('Entrada Invalida!') 
        sleep(2)
        os.system('cls')
