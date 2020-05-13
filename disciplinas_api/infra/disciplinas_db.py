import sqlite3

db_name = "disciplinas.db"
table_name = "disciplina"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY AUTOINCREMENT, nome text NOT NULL UNIQUE, professor_id int NOT NULL)"


def createTable(cursor, sql):
    cursor.execute(sql)


def popularDb(cursor, nome, professor_id):
    sql = f"INSERT INTO {table_name} (nome, professor_id) VALUES (?, ?)"
    cursor.execute(sql, (nome, professor_id))


def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, "Desenvolvimento de aplic. distribuidas", 1)
        popularDb(cursor, "Estrutura de dados", 2)
        popularDb(cursor, "LPT 1", 3)
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()


init()
