import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.classes.Registro import Registro

class InterfaceRegistro(ttk.Frame):
    def __init__(self, parent, showListarNaves):
        super().__init__(parent)
        self.showListarNaves = showListarNaves

        self.registro = Registro()

        # opcoes para registro
        self.menuOpt = {}
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
            "periculosidade": tk.StringVar(self)
        }

        # registro
        self.vcmd = (self.register(self.validate))
        self.getInfo()
        self.nomeLabel = ttk.Label(self, text="Nome da nave", font=('Comic Sans MS', 12))
        self.nome = ttk.Entry(self, textvariable=self.optValue['nome'])
        self.tamanhoLabel = ttk.Label(self, text="Tamanho da nave", font=('Comic Sans MS', 12))
        self.tamanho = ttk.OptionMenu(self, self.optValue['tamanho'], self.menuOpt['tamanho'][0], *self.menuOpt['tamanho'])
        self.corLabel = ttk.Label(self, text="Cor da nave", font=('Comic Sans MS', 12))
        self.cor = ttk.OptionMenu(self, self.optValue['cor'], self.menuOpt['cor'][0], *self.menuOpt['cor'])
        self.localLabel = ttk.Label(self, text="Local da queda", font=('Comic Sans MS', 12))
        self.local = ttk.OptionMenu(self, self.optValue['local_queda'], self.menuOpt['local_queda'][0], *self.menuOpt['local_queda'])
        self.poderLabel = ttk.Label(self, text="Poderio bélico", font=('Comic Sans MS', 12))
        self.poder = ttk.OptionMenu(self, self.optValue['poderio'], self.menuOpt['poderio'][0], *self.menuOpt['poderio'])
        self.armamentoLabel = ttk.Label(self, text="Armamento", font=('Comic Sans MS', 12))
        self.armamento = tk.Listbox(self, self.optValue['armas'], selectmode="multiple", exportselection=0)
        for item in self.menuOpt['armas']:
            self.armamento.insert(self.menuOpt['armas'].index(item), item)

        self.combustivelLabel = ttk.Label(self, text="Combustível", font=('Comic Sans MS', 12))
        self.combustivel = ttk.OptionMenu(self, self.optValue['combustiveis'], self.menuOpt['combustiveis'][0], *self.menuOpt['combustiveis'])
        self.qtdSobreviventeLabel = ttk.Label(self, text="Número de sobreviventes", font=('Comic Sans MS', 12))
        self.qtdSobrevivente = ttk.Entry(self, textvariable=self.optValue['qtdSobrevivente'], validate='all', validatecommand=(self.vcmd, '%P'))
        self.estadoSobreviventeLabel = ttk.Label(self, text="Estado dos sobreviventes", font=('Comic Sans MS', 12))
        self.estadoSobrevivente = ttk.OptionMenu(self, self.optValue['trip_estado'], self.menuOpt['trip_estado'][0], *self.menuOpt['trip_estado'])
        self.avariaLabel = ttk.Label(self, text="Grau de avaria", font=('Comic Sans MS', 12))
        self.avaria = ttk.OptionMenu(self, self.optValue['avaria'], self.menuOpt['avaria'][0], *self.menuOpt['avaria'])
        self.potencialLabel = ttk.Label(self, text="Potencial de prospecção tecnológica", font=('Comic Sans MS', 12))
        self.potencial = ttk.OptionMenu(self, self.optValue['potencial'], self.menuOpt['potencial'][0], *self.menuOpt['potencial'])
        self.periculosidadeLabel = ttk.Label(self, text="Grau de periculosidade", font=('Comic Sans MS', 12))
        self.periculosidade = ttk.OptionMenu(self, self.optValue['periculosidade'], self.menuOpt['periculosidade'][0], *self.menuOpt['periculosidade'])

        self.buttomVoltar = ttk.Button(self, text="Voltar", command=self.showMain)
        self.buttom = ttk.Button(self, text="Enviar", command=self.registrar)
    
    def validate(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    
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
    
    def registrar(self):
        data = {}
        data['nome'] = self.menuOpt['nome'].get()
        data['tamanho'] = self.menuOpt['tamanho'].index(self.optValue['tamanho'].get()) # int
        data['cor'] = self.menuOpt['cor'].index(self.optValue['cor'].get()) # int
        data['local_queda'] = self.optValue['local_queda'].get() # text
        data['combustivel'] = self.optValue['combustiveis'].get() # text
        if (self.optValue['qtdSobrevivente'].get() == ''):
            data['trip_sobrevivente'] = 0
        else:
            data['trip_sobrevivente'] = int(self.optValue['qtdSobrevivente'].get()) # int
        data['trip_estado'] = self.optValue['trip_estado'].get() # text
        data['avaria'] = self.menuOpt['avaria'].index(self.optValue['avaria'].get()) # int
        data['potencial'] = self.menuOpt['potencial'].index(self.optValue['potencial'].get()) # int
        data['periculosidade'] = self.menuOpt['periculosidade'].index(self.optValue['periculosidade'].get()) # int

        reslist = list()
        combinacaoValor = 0
        selectionArmas = self.armamento.curselection()

        if (len(selectionArmas) != 0):
            for i in selectionArmas:
                entrada = self.armamento.get(i)
                reslist.append(entrada)
                
                indexArmas = self.menuOpt['armas'].index(entrada)
                combinacaoValor += 2**indexArmas
        combinacaoValor += 256 * self.menuOpt['poderio'].index(self.optValue['poderio'].get())

        data['armamento'] = combinacaoValor # int

        response = self.registro.inserir(data)
        if (response == 200):
            messagebox.showinfo("Sucesso", "Nave registrada com sucesso")
        else:
            messagebox.showerror("Ops!", "Algo deu errado =(")
        
        self.resetValues()
        self.showMain()
    
    def getInfo(self):
        with open("src/options.json", "r", encoding='utf-8') as f:
            self.menuOpt = json.load(f)

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
