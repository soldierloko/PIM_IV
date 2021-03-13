import sqlite3

# conectando...
conn = sqlite3.connect('SRE.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  CLIENTES (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        dtNascimento DATE NOT NULL,
        classificacao INT NOT NULL,
        criado_em DATE NOT NULL
);""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()

