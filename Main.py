#Importa as Bibliotecas necessárias
import Funcoes as fc
from time import sleep
from Classes import Aluno_Professor
import os

#Faça Até que eu mande Sair do Sistema
while True:
    #Apaga a tela
    os.system('cls') or None
    #Chama o Menu Principal
    fc.exibir_menu()
    #Aguarda o user entrar com uma opção
    opcao = int(input('Digite uma opção: '))
    #Abre o script de acordo com a opção do usuário
    if opcao == 1:
        os.system('cls') or None
        fc.cadastro()
    elif opcao == 2:
        os.system('cls') or None
        fc.equipamento()
    elif opcao == 3:
        os.system('cls') or None
        fc.reserva()
    
        
    elif opcao == 6:
        print("Fechando programa!")
        sleep(2)
        os.system('cls') or None
        break
    else:
        print('Opção inválida')


