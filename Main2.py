#Importa as Bibliotecas necessárias
import Funcoes as fc
from time import sleep
from Classes import Aluno_Professor
import os


while True:
    fc.exibir_menu()
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        os.system('cls') or None
        fc.cadastro()

        
    # elif opcao == 2:
    #     fc.listar(pessoas)
    # elif opcao == 3:
    #     fc.buscar(pessoas)
    elif opcao == 5:
        print("Fechando programa!")
        sleep(2)
        os.system('cls') or None
        break
    else:
        print('Opção inválida')


