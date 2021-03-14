import sqlite3

# conectando...
conn = sqlite3.connect('SRE.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  TD_CLIENTES (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        dtNascimento DATE NOT NULL,
        classificacao INT NOT NULL,
        criado_em DATE NOT NULL
);""")

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  TD_USUARIO (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        dtCadastro DATE NOT NULL,
        ativo INTEGER NOT NULL
);""")


# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  TD_EQUIPAMENTO (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        dtReserva DATE NULL,
        dtRetira DATE NULL,
        dtDevolucao DATE NULL,
        criado_em DATE NOT NULL
);""")

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  TF_COMODATO (
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

