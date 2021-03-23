import sqlite3

# conectando...
conn = sqlite3.connect('SRE.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  TD_CADASTRO (
        Aluno_Professor TEXT NOT NULL,
        matricula TEXT NOT NULL,
        nome TEXT NOT NULL,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        dtNascimento DATE NOT NULL,
        criado_em DATE NOT NULL
);""")

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  TD_EQUIPAMENTO (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        numSerie LONG NOT NULL,
        desDescricao TEXT NOT NULL,
        dtCompra DATE NULL,
        desTipo TEXT NOT NULL,
        desMarca TEXT NOT NULL,
        criado_em DATE NOT NULL
);""")

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  TF_COMODATO (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        matAluno_Professor TEXT NOT NULL,
        idEquipamento INTEGER NOT NULL,
        dtReserva DATE NOT NULL,
        criado_em DATE NOT NULL,
        idDevolvido INTEGER NOT NULL,
        dtDevolução DATE NULL);""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()

