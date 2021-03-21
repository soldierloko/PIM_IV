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

def cadastrar(pessoas):
    identificador = input('Id? ')
    nome = input('Nome? ')
    idade = int(input('Idade? '))
    pessoas.append((identificador, nome, idade))

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