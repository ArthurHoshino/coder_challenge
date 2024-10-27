import sqlite3, json
from contextlib import closing

class Registro:
    def __init__(self):
        self.criarTabelas()
        self.classificacaoMetrica = {
            "Sucata Espacial": {
                "poderio": [0],
                "armas": [],
                "combustivel": [],
                "avaria": [3, 4, 5],
                "potencial": [0],
                "periculosidade": [0, 1],
                "qtdInfo": [0]
            },
            "Joia Tecnológica": {
                "poderio": [0],
                "armas": [0, 1, 2],
                "combustivel": [],
                "avaria": [0, 1, 2],
                "potencial": [2, 3],
                "periculosidade": [0, 1],
                "qtdInfo": [0, 1]
            },
            "Arsenal Alienígena": {
                "poderio": [2, 3],
                "armas": [3, 4, 5],
                "combustivel": [],
                "avaria": [0, 1],
                "potencial": [1, 2, 3],
                "periculosidade": [2],
                "qtdInfo": [0, 1]
            },
            "Ameaça em Potencial": {
                "poderio": [2, 3],
                "armas": [6, 7, 8],
                "combustivel": [2, 5, 6],
                "avaria": [0, 1, 2, 3],
                "potencial": [2, 3],
                "periculosidade": [2, 3],
                "qtdInfo": [0, 1]
            },
            "Fonte de Energia Alternativa": {
                "poderio": [0, 1],
                "armas": [0, 1],
                "combustivel": [2, 3, 4],
                "avaria": [0, 1, 2],
                "potencial": [1, 2, 3],
                "periculosidade": [0, 1],
                "qtdInfo": [0, 1]
            },
            "Enigma Científico": {
                "poderio": [0, 1],
                "armas": [0, 1, 2],
                "combustivel": [],
                "avaria": [0, 1, 2, 3],
                "potencial": [3],
                "periculosidade": [0, 1],
                "qtdInfo": [2, 3]
            },
            "Biblioteca Intergalática": {
                "poderio": [0],
                "armas": [0, 1],
                "combustivel": [],
                "avaria": [0, 1],
                "potencial": [0, 1, 2],
                "periculosidade": [0],
                "qtdInfo": [2, 3]
            }
        }

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
                            qtd_info INTEGER,
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
                            qtd_info INTEGER,
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
                        qtd_info INTEGER,
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
                            qtd_info,
                            classificacao,
                            created_at,
                            updated_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
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
                        data['info'],
                        classificacao
                    ))
                    connection.commit()
                except Exception as e:
                    connection.rollback()
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
                            qtd_info = ?,
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
                        data['info'],
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
                            qtd_info,
                            classificacao,
                            deleted_at           
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    """, (
                        row[0], # id
                        row[1], # nome
                        row[2], # tamanho
                        row[3], # cor
                        row[4], # local_queda
                        row[5], # armamento
                        row[6], # combustivel
                        row[7], # sobrevivente
                        row[8], # estado
                        row[9], # avaria
                        row[10], # potencial
                        row[11], # periculosidade
                        row[12], # info
                        row[13],
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
        classificacaoPonto = {
            "Ameaça em Potencial": 0,
            "Arsenal Alienígena": 0,
            "Joia Tecnológica": 0,
            "Biblioteca Intergalática": 0,
            "Enigma Científico": 0,
            "Fonte de Energia Alternativa": 0,
            "Sucata Espacial": 0
        }

        with open("src/options.json", "r", encoding='utf-8') as f:
            d = json.load(f)
            combustivelOpt = d['combustiveis']

        armasData = format((data['armamento'] % 256), 'b')
        qtdArmas = 0
        for i in armasData:
            if (i == '1'):
                qtdArmas += 1

        naveDados = {
            "poderio": data['armamento'] // 256,
            "armas": qtdArmas,
            "combustivel": combustivelOpt.index(data['combustivel']),
            "avaria": data['avaria'],
            "potencial": data['potencial'],
            "periculosidade": data['periculosidade'],
            "qtdInfo": data['info']
        }

        for i, j in self.classificacaoMetrica.items():
            for x, y in zip(j.values(), naveDados.values()):
                if (len(x) != 0 and y in x):
                    classificacaoPonto[i] += 1
            
        # print(classificacaoPonto)
        classificacao = max(classificacaoPonto, key=classificacaoPonto.get)
        
        return classificacao

