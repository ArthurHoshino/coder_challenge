import sqlite3
from contextlib import closing

class Registro:
    def __init__(self):
        pass

    def criarTabelas(self):
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("""
                    CREATE TABLE naves(
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
                    )
                """)
    
    def resetarTabela(self):
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("DROP TABLE naves")
                cursor.execute("""
                    CREATE TABLE naves(
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
                    )
                """)
    
    def inserir(self, data: dict):
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                try:
                    cursor.execute("""
                        INSERT INTO naves (
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
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (data['tamanho'],
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
                except Exception as e:
                    print(e)
        
    def gerarClassificacao(self, data: dict):
        pass

