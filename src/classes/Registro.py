import sqlite3

class Registro:
    def __init__(self, tamanho: list, cor: list, localQueda: list, poderioBelico: list, armamento: list, combustivel: list, tripulacao_estado: list, avaria: list, potencial_tech: list, peric: list):
        self.connection = sqlite3.connect("teste.db")
        

    def criarTabelas(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE estado_nave(
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
    
    def inserirValoresTeste(self):
        cursor = self.connection.cursor()

        # pegar os inputs pelo tkinter
