import sqlite3

def listar_cadastro(cpf):
    #Abrindo conexão com o BD para persistir ou consultar dados
    conn = sqlite3.connect('SRE.db')
    cursor = conn.cursor()
    
    #Busca o usuário
    query = "SELECT * FROM TD_CADASTRO WHERE CPF LIKE '%" + cpf + "%'"
    cursor.execute(query)
    
    for linha in cursor.fetchall():
        nome = linha[2]
        matricula = linha[1]
    #Fecha a conexão
    conn.close()
    return matricula,nome


print(listar_cadastro('339')[0])

#if listar_cadastro('339') != None:
 #       print('Usuário não encontrado')