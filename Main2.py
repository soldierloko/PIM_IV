# def main():
#     pessoas = []
from Funcoes import * as fc

while True:
    fc.exibir_menu()
    opcao = int(input('Opção? '))
    if opcao == 1:
        cadastrar(pessoas)
    elif opcao == 2:
        listar(pessoas)
    elif opcao == 3:
        buscar(pessoas)
    else:
        print('Opção inválida')