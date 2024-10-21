import json
import tkinter as tk
from tkinter import ttk
from src.classes.Registro import Registro

class InterfaceIndex:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x650")
        self.root.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.registro = Registro()
        self.showFunctions = {
            "main": self.showMain,
            "registro": self.showRegistro
        }

        # opcoes para registro
        self.menuOpt = {}
        self.optValue = {
            "tamanho": tk.StringVar(self.root),
            "cor": tk.StringVar(self.root),
            "local_queda": tk.StringVar(self.root),
            "poderio": tk.StringVar(self.root),
            "armas": list(),
            "combustiveis": tk.StringVar(self.root),
            "qtdSobrevivente": tk.StringVar(self.root),
            "trip_estado": tk.StringVar(self.root),
            "avaria": tk.StringVar(self.root),
            "potencial": tk.StringVar(self.root),
            "periculosidade": tk.StringVar(self.root)
        }

        # main
        self.buttonRegistro = ttk.Button(self.root, text="Registrar nave", command=self.showFunctions['registro'])
        self.buttonVisualizar = ttk.Button(self.root, text="Visualizar naves")

        # registro
        self.tamanhoLabel = None
        self.tamanho = None
        self.corLabel = None
        self.cor = None
        self.localLabel = None
        self.local = None
        self.poderLabel = None
        self.poder = None
        self.armamentoLabel = None
        self.armamento = None
        self.combustivelLabel = None
        self.combustivel = None
        self.qtdSobreviventeLabel = None
        self.qtdSobrevivente = None
        self.estadoSobreviventeLabel = None
        self.estadoSobrevivente = None
        self.avariaLabel = None
        self.avaria = None
        self.potencialLabel = None
        self.potencial = None
        self.periculosidadeLabel = None
        self.periculosidade = None
        self.buttom = ttk.Button(self.root, text="Enviar", command=self.registrar)
        self.buttomVoltar = ttk.Button(self.root, text="Voltar", command=self.showFunctions['main'])
        self.vcmd = (self.root.register(self.validate))

    def getOptions(self):
        with open("src/options.json", "r", encoding='utf-8') as f:
            self.menuOpt = json.load(f)

        self.tamanhoLabel = ttk.Label(self.root, text="Tamanho da nave", font=('Comic Sans MS', 14))
        self.tamanho = ttk.OptionMenu(self.root, self.optValue['tamanho'], self.menuOpt['tamanho'][0], *self.menuOpt['tamanho'])
        self.corLabel = ttk.Label(self.root, text="Cor da nave", font=('Comic Sans MS', 14))
        self.cor = ttk.OptionMenu(self.root, self.optValue['cor'], self.menuOpt['cor'][0], *self.menuOpt['cor'])
        self.localLabel = ttk.Label(self.root, text="Local da queda", font=('Comic Sans MS', 14))
        self.local = ttk.OptionMenu(self.root, self.optValue['local_queda'], self.menuOpt['local_queda'][0], *self.menuOpt['local_queda'])
        self.poderLabel = ttk.Label(self.root, text="Poderio bélico", font=('Comic Sans MS', 14))
        self.poder = ttk.OptionMenu(self.root, self.optValue['poderio'], self.menuOpt['poderio'][0], *self.menuOpt['poderio'])
        self.armamentoLabel = ttk.Label(self.root, text="Armamento", font=('Comic Sans MS', 14))
        self.armamento = tk.Listbox(self.root, self.optValue['armas'], selectmode="multiple", exportselection=0)
        for item in self.menuOpt['armas']:
            self.armamento.insert(self.menuOpt['armas'].index(item), item)

        self.combustivelLabel = ttk.Label(self.root, text="Combustível", font=('Comic Sans MS', 14))
        self.combustivel = ttk.OptionMenu(self.root, self.optValue['combustiveis'], self.menuOpt['combustiveis'][0], *self.menuOpt['combustiveis'])
        self.qtdSobreviventeLabel = ttk.Label(self.root, text="Número de sobreviventes", font=('Comic Sans MS', 14))
        self.qtdSobrevivente = ttk.Entry(self.root, textvariable=self.optValue['qtdSobrevivente'], validate='all', validatecommand=(self.vcmd, '%P'))
        self.estadoSobreviventeLabel = ttk.Label(self.root, text="Estado dos sobreviventes", font=('Comic Sans MS', 14))
        self.estadoSobrevivente = ttk.OptionMenu(self.root, self.optValue['trip_estado'], self.menuOpt['trip_estado'][0], *self.menuOpt['trip_estado'])
        self.avariaLabel = ttk.Label(self.root, text="Grau de avaria", font=('Comic Sans MS', 14))
        self.avaria = ttk.OptionMenu(self.root, self.optValue['avaria'], self.menuOpt['avaria'][0], *self.menuOpt['avaria'])
        self.potencialLabel = ttk.Label(self.root, text="Potencial de prospecção tecnológica", font=('Comic Sans MS', 14))
        self.potencial = ttk.OptionMenu(self.root, self.optValue['potencial'], self.menuOpt['potencial'][0], *self.menuOpt['potencial'])
        self.periculosidadeLabel = ttk.Label(self.root, text="Grau de periculosidade", font=('Comic Sans MS', 14))
        self.periculosidade = ttk.OptionMenu(self.root, self.optValue['periculosidade'], self.menuOpt['periculosidade'][0], *self.menuOpt['periculosidade'])

    def hide_all(self):
        self.hideMain()
        self.hideRegistro()
    
    def validate(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    
    def registrar(self):
        data = {}
        data['tamanho'] = self.menuOpt['tamanho'].index(self.optValue['tamanho'].get()) # int
        data['cor'] = self.menuOpt['cor'].index(self.optValue['cor'].get()) # int
        data['local_queda'] = self.optValue['local_queda'].get() # text
        data['combustivel'] = self.optValue['combustiveis'].get() # text
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

        self.registro.inserir(data)
    
    # show functions
    def showMain(self):
        self.hide_all()
        self.buttonRegistro.pack(padx=20, pady=12)
        self.buttonVisualizar.pack(padx=20, pady=12)

    def showRegistro(self):
        self.hide_all()

        self.tamanhoLabel.grid(row=0, column=0, padx=10, pady=20, sticky=tk.EW)
        self.tamanho.grid(row=0, column=1, padx=10, pady=20, sticky='ew')
        self.corLabel.grid(row=1, column=0, padx=10, pady=20, sticky='ew')
        self.cor.grid(row=1, column=1, padx=10, pady=20, sticky='ew')
        self.localLabel.grid(row=2, column=0, padx=10, pady=20, sticky='ew')
        self.local.grid(row=2, column=1, padx=10, pady=20, sticky='ew')
        self.poderLabel.grid(row=3, column=0, padx=10, pady=20, sticky='ew')
        self.poder.grid(row=3, column=1, padx=10, pady=20, sticky='ew')
        self.armamentoLabel.grid(row=4, column=0, padx=10, pady=20, sticky='ew')
        self.armamento.grid(row=4, column=1, padx=10, pady=20, sticky='ew')
        self.combustivelLabel.grid(row=5, column=0, padx=10, pady=20, sticky='ew')
        self.combustivel.grid(row=5, column=1, padx=10, pady=20, sticky='ew')
        self.qtdSobreviventeLabel.grid(row=0, column=2, padx=10, pady=20, sticky='ew')
        self.qtdSobrevivente.grid(row=0, column=3, padx=10, pady=20, sticky='ew')
        self.estadoSobreviventeLabel.grid(row=1, column=2, padx=10, pady=20, sticky='ew')
        self.estadoSobrevivente.grid(row=1, column=3, padx=10, pady=20, sticky='ew')
        self.avariaLabel.grid(row=2, column=2, padx=10, pady=20, sticky='ew')
        self.avaria.grid(row=2, column=3, padx=10, pady=20, sticky='ew')
        self.potencialLabel.grid(row=3, column=2, padx=10, pady=20, sticky='ew')
        self.potencial.grid(row=3, column=3, padx=10, pady=20, sticky='ew')
        self.periculosidadeLabel.grid(row=4, column=2, padx=10, pady=20, sticky='ew')
        self.periculosidade.grid(row=4, column=3, padx=10, pady=20, sticky='ew')

        self.buttomVoltar.grid(row=11, column=0, padx=20, pady=20, sticky='w', columnspan=2)
        self.buttom.grid(row=11, column=2, padx=20, pady=20, sticky='w', columnspan=2)

    # hide functions
    def hideMain(self):
        self.buttonRegistro.pack_forget()
        self.buttonVisualizar.pack_forget()

    def hideRegistro(self):
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

    def run(self):
        self.getOptions()
        self.showMain()
        self.root.mainloop()

    
    
    
    
    
