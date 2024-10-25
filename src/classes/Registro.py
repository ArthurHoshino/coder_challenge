import sqlite3
from contextlib import closing

class Registro:
    def __init__(self):
        self.criarTabelas()

    def criarTabelas(self):
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                try:
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
                            classificacao TEXT,
                            created_at TEXT,
                            updated_at TEXT
                        );
                    """)
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS naves_deletadas(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nave_id INTEGER NOT NULL,
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
                            classificacao TEXT,
                            deleted_at TEXT
                        );
                    ''')
                except sqlite3.IntegrityError:
                    connection.rollback()

    
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
                classificacao = self.gerarClassificacao(data)
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
                            classificacao,
                            created_at,
                            updated_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
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
                        classificacao
                    ))
                    connection.commit()
                except Exception as e:
                    print(e)
                    retorno = 500
        return retorno

    def editar(self, data: dict):
        retorno = 200
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                classificacao = self.gerarClassificacao(data)
                try:
                    cursor.execute("""
                        UPDATE naves SET
                            nome= ?,
                            tamanho= ?,
                            cor= ?,
                            local_queda= ?,
                            armamento= ?,
                            combustivel= ?,
                            tripulacao_sobrevivente= ?,
                            tripulacao_estado= ?,
                            avaria= ?,
                            potencial_tech= ?,
                            grau_periculosidade= ?,
                            classificacao= ?,
                            updated_at = CURRENT_TIMESTAMP
                        WHERE id = ?;
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
                        classificacao,
                        data['id'],
                    ))
                    connection.commit()
                except Exception as e:
                    print(e)
                    retorno = 500
        return retorno

    def deletar(self, id):
        retorno = 200
        with closing(sqlite3.connect("coderchallenge.db")) as connection:
            with closing(connection.cursor()) as cursor:
                try:
                    row = cursor.execute("""
                        SELECT * FROM naves WHERE id = ?
                    """, (id,)).fetchone()

                    cursor.execute("""
                        INSERT INTO naves_deletadas (
                            nave_id,
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
                            classificacao,
                            deleted_at           
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    """, (
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                    ))

                    cursor.execute("""
                        DELETE FROM naves
                        WHERE id = ?
                    """, (id,))

                    connection.commit()
                except Exception as e:
                    connection.rollback()
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
                """, (id,)).fetchone()
        
        return row
        
    def gerarClassificacao(self, data: dict):
        return "Classificacao Placeholder"

