import sqlite3

def listar_cadastro(cpf):
    #Abrindo conexão com o BD para persistir ou consultar dados
    conn = sqlite3.connect('SRE.db')
    cursor = conn.cursor()
    
    #Busca o usuário
    cursor.execute("SELECT * FROM TD_CADASTRO WHERE CPF LIKE '" + cpf + "'")
    
    for linha in cursor.fetchall():
        print(linha)

    
    # except:
    #     print("Usuário Não encontrado")
    #Fecha instancia com o BD
    conn.close()
    return

listar_cadastro('339')