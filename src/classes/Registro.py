import sqlite3
from contextlib import closing

class Registro:
    def __init__(self):
        self.criarTabelas()

    def criarTabelas(self):
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS naves(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        tamanho INTEGER,
                        cor INTEGER,
                        local_queda TEXT,
                        armamento INTEGER,
                        combustivel TEXT,
                        tripulacao_sobrevivente INTEGER,
                        tripulacao_estado TEXT,
                        avaria INTEGER,
                        potencial_tech INTEGER,
                        grau_periculosidade INTEGER,
                        classificacao TEXT
                    );
                """)
    
    def resetarTabela(self):
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("DROP TABLE naves")
                cursor.execute("""
                    CREATE TABLE naves(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        tamanho INTEGER,
                        cor INTEGER,
                        local_queda TEXT,
                        armamento INTEGER,
                        combustivel TEXT,
                        tripulacao_sobrevivente INTEGER,
                        tripulacao_estado TEXT,
                        avaria INTEGER,
                        potencial_tech INTEGER,
                        grau_periculosidade INTEGER,
                        classificacao TEXT
                    );
                """)
    
    def inserir(self, data: dict):
        retorno = 200
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                try:
                    cursor.execute("""
                        INSERT INTO naves (
                            nome,
                            tamanho,
                            cor,
                            local_queda,
                            armamento,
                            combustivel,
                            tripulacao_sobrevivente,
                            tripulacao_estado,
                            avaria,
                            potencial_tech,
                            grau_periculosidade,
                            classificacao
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    """, (data['nome'],
                        data['tamanho'],
                        data['cor'],
                        data['local_queda'],
                        data['armamento'],
                        data['combustivel'],
                        data['trip_sobrevivente'],
                        data['trip_estado'],
                        data['avaria'],
                        data['potencial'],
                        data['periculosidade'],
                        "Classificacao Placeholder"
                    ))
                    connection.commit()
                except Exception as e:
                    print(e)
                    retorno = 500
        return retorno

    def getAllNaves(self):
        rows = list()
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                rows = cursor.execute("""
                    SELECT id, nome FROM naves
                """).fetchall()
        
        return rows

    def getNaveById(self, id):
        row = list()
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                row = cursor.execute("""
                    SELECT * FROM naves
                    WHERE naves.id = ?
                """, (id,)).fetchall()
        
        return row
        
    def gerarClassificacao(self, data: dict):
        pass

