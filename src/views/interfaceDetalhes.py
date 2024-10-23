import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.classes.Registro import Registro

class InterfaceRegistro(ttk.Frame):
    def __init__(self, parent, showListarNaves, showEditar, naveId):
        super().__init__(parent)
        self.showListarNaves = showListarNaves
        self.showEditar = showEditar
        self.naveId = naveId

        self.registro = Registro()

        # opcoes para registro
        self.armasOpt = []
        self.optValue = {
            "nome": tk.StringVar(self),
            "tamanho": tk.StringVar(self),
            "cor": tk.StringVar(self),
            "local_queda": tk.StringVar(self),
            "poderio": tk.StringVar(self),
            "armas": list(),
            "combustiveis": tk.StringVar(self),
            "qtdSobrevivente": tk.StringVar(self),
            "trip_estado": tk.StringVar(self),
            "avaria": tk.StringVar(self),
            "potencial": tk.StringVar(self),
            "periculosidade": tk.StringVar(self),
            "classificacao": tk.StringVar(self)
        }

        # registro
        self.vcmd = (self.register(self.validate))
        self.getInfo()
        self.nomeLabel = ttk.Label(self, text="Nome da nave", font=('Comic Sans MS', 12))
        self.nome = ttk.Entry(self, textvariable=self.optValue['nome'])
        self.tamanhoLabel = ttk.Label(self, text="Tamanho da nave", font=('Comic Sans MS', 12))
        self.tamanho = ttk.Entry(self, textvariable=self.optValue['tamanho'])
        self.corLabel = ttk.Label(self, text="Cor da nave", font=('Comic Sans MS', 12))
        self.cor = ttk.Entry(self, textvariable=self.optValue['cor'])
        self.localLabel = ttk.Label(self, text="Local da queda", font=('Comic Sans MS', 12))
        self.local = ttk.Entry(self, textvariable=self.optValue['local_queda'])
        self.poderLabel = ttk.Label(self, text="Poderio bélico", font=('Comic Sans MS', 12))
        self.poder = ttk.Entry(self, textvariable=self.optValue['poderio'])
        self.armamentoLabel = ttk.Label(self, text="Armamento", font=('Comic Sans MS', 12))
        self.armamento = tk.Listbox(self, self.optValue['armas'], selectmode="multiple", exportselection=0)
        for item in self.armasOpt:
            self.armamento.insert(self.armasOpt.index(item), item)

        self.combustivelLabel = ttk.Label(self, text="Combustível", font=('Comic Sans MS', 12))
        self.combustivel = ttk.Entry(self, textvariable=self.optValue['combustiveis'])
        self.qtdSobreviventeLabel = ttk.Label(self, text="Número de sobreviventes", font=('Comic Sans MS', 12))
        self.qtdSobrevivente = ttk.Entry(self, textvariable=self.optValue['qtdSobrevivente'])
        self.estadoSobreviventeLabel = ttk.Label(self, text="Estado dos sobreviventes", font=('Comic Sans MS', 12))
        self.estadoSobrevivente = ttk.Entry(self, textvariable=self.optValue['trip_estado'])
        self.avariaLabel = ttk.Label(self, text="Grau de avaria", font=('Comic Sans MS', 12))
        self.avaria = ttk.Entry(self, textvariable=self.optValue['avaria'])
        self.potencialLabel = ttk.Label(self, text="Potencial de prospecção tecnológica", font=('Comic Sans MS', 12))
        self.potencial = ttk.Entry(self, textvariable=self.optValue['potencial'])
        self.periculosidadeLabel = ttk.Label(self, text="Grau de periculosidade", font=('Comic Sans MS', 12))
        self.periculosidade = ttk.Entry(self, textvariable=self.optValue['periculosidade'])
        self.classificacaoLabel = ttk.Label(self, text="Classificação", font=('Comic Sans MS', 12))
        self.classificacao = ttk.Entry(self, textvariable=self.optValue['classificacao'])

        self.buttomVoltar = ttk.Button(self, text="Voltar", command=self.showMain)
        self.buttom = ttk.Button(self, text="Editar")

        self.nome.configure(state='disable')
        self.tamanho.configure(state='disable')
        self.cor.configure(state='disable')
        self.local.configure(state='disable')
        self.poder.configure(state='disable')
        self.armamento.configure(state='disable')
        self.combustivel.configure(state='disable')
        self.qtdSobrevivente.configure(state='disable')
        self.estadoSobrevivente.configure(state='disable')
        self.avaria.configure(state='disable')
        self.potencial.configure(state='disable')
        self.periculosidade.configure(state='disable')
        self.classificacao.configure(state='disable')
    
    def getInfo(self):
        with open("src/options.json", "r", encoding='utf-8') as f:
            allOpt = json.load(f)
        response = self.registro.getNaveById(self.naveId)

        self.nome.insert(response[1])
        self.tamanho.insert(allOpt[response[2]])
        self.cor.insert(allOpt[response[3]])
        self.local.insert(response[4])
        self.poder.insert( allOpt[ response[5] // 256 ] )
        # logica das armas selecionadas
        armasSelecionadas = format((response[5] % 256), 'b')[::-1]
        for arma in armasSelecionadas:
            print(arma)

        self.combustivel.insert(response[6])
        self.qtdSobrevivente.insert(response[7])
        self.estadoSobrevivente.insert(response[8])
        self.avaria.insert(allOpt[response[9]])
        self.potencial.insert(allOpt[response[10]])
        self.periculosidade.insert(allOpt[response[11]])
        self.classificacao.insert(response[12])
    
    def resetValues(self):
        self.optValue = {
            "tamanho": tk.StringVar(self),
            "cor": tk.StringVar(self),
            "local_queda": tk.StringVar(self),
            "poderio": tk.StringVar(self),
            "armas": list(),
            "combustiveis": tk.StringVar(self),
            "qtdSobrevivente": tk.StringVar(self),
            "trip_estado": tk.StringVar(self),
            "avaria": tk.StringVar(self),
            "potencial": tk.StringVar(self),
            "periculosidade": tk.StringVar(self)
        }
        

    def show(self):
        self.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.95, anchor='center')
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1, uniform='a')

        self.nomeLabel.grid(row=0, column=0, padx=10, pady=20, sticky='nsew')
        self.nome.grid(row=0, column=1, padx=10, pady=20, sticky='nsew')

        self.tamanhoLabel.grid(row=1, column=0, padx=10, pady=20, sticky='nsew')
        self.tamanho.grid(row=1, column=1, padx=10, pady=20, sticky='nsew')
        self.corLabel.grid(row=2, column=0, padx=10, pady=20, sticky='nsew')
        self.cor.grid(row=2, column=1, padx=10, pady=20, sticky='nsew')
        self.localLabel.grid(row=3, column=0, padx=10, pady=20, sticky='nsew')
        self.local.grid(row=3, column=1, padx=10, pady=20, sticky='nsew')
        self.poderLabel.grid(row=4, column=0, padx=10, pady=20, sticky='nsew')
        self.poder.grid(row=4, column=1, padx=10, pady=20, sticky='nsew')
        self.armamentoLabel.grid(row=5, column=0, padx=10, pady=20, sticky='nsew', rowspan=2)
        self.armamento.grid(row=5, column=1, padx=10, pady=20, sticky='nsew', rowspan=2)

        self.qtdSobreviventeLabel.grid(row=0, column=2, padx=10, pady=20, sticky='nsew')
        self.qtdSobrevivente.grid(row=0, column=3, padx=10, pady=20, sticky='nsew')
        self.estadoSobreviventeLabel.grid(row=1, column=2, padx=10, pady=20, sticky='nsew')
        self.estadoSobrevivente.grid(row=1, column=3, padx=10, pady=20, sticky='nsew')
        self.avariaLabel.grid(row=2, column=2, padx=10, pady=20, sticky='nsew')
        self.avaria.grid(row=2, column=3, padx=10, pady=20, sticky='nsew')
        self.potencialLabel.grid(row=3, column=2, padx=10, pady=20, sticky='nsew')
        self.potencial.grid(row=3, column=3, padx=10, pady=20, sticky='nsew')
        self.periculosidadeLabel.grid(row=4, column=2, padx=10, pady=20, sticky='nsew')
        self.periculosidade.grid(row=4, column=3, padx=10, pady=20, sticky='nsew')
        self.combustivelLabel.grid(row=5, column=2, padx=10, pady=20, sticky='nsew')
        self.combustivel.grid(row=5, column=3, padx=10, pady=20, sticky='nsew')

        self.buttomVoltar.grid(row=7, column=0, padx=20, pady=20, sticky='nsew', columnspan=2)
        self.buttom.grid(row=7, column=2, padx=20, pady=20, sticky='nsew', columnspan=2)
    
    def hide(self):
        self.nomeLabel.grid_forget()
        self.nome.grid_forget()
        self.tamanhoLabel.grid_forget()
        self.tamanho.grid_forget()
        self.corLabel.grid_forget()
        self.cor.grid_forget()
        self.localLabel.grid_forget()
        self.local.grid_forget()
        self.poderLabel.grid_forget()
        self.poder.grid_forget()
        self.armamentoLabel.grid_forget()
        self.armamento.grid_forget()
        self.combustivelLabel.grid_forget()
        self.combustivel.grid_forget()
        self.qtdSobreviventeLabel.grid_forget()
        self.qtdSobrevivente.grid_forget()
        self.estadoSobreviventeLabel.grid_forget()
        self.estadoSobrevivente.grid_forget()
        self.avariaLabel.grid_forget()
        self.avaria.grid_forget()
        self.potencialLabel.grid_forget()
        self.potencial.grid_forget()
        self.periculosidadeLabel.grid_forget()
        self.periculosidade.grid_forget()
        self.buttom.grid_forget()
        self.buttomVoltar.grid_forget()
        self.place_forget()
