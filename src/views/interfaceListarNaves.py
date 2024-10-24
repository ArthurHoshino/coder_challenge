import tkinter as tk
from tkinter import ttk
from src.classes.Registro import Registro

class InterfaceListarNaves(ttk.Frame):
    def __init__(self, parent, showMain, showDetalhes):
        super().__init__(parent)
        self.registro = Registro()
        self.showMain = showMain
        self.showDetalhes = showDetalhes
        self.rows = list()
        self.navesNomes = list()
        self.opt = tk.StringVar(self)

        # campos
        self.getInfo()
        self.label = ttk.Label(self, text="Selecione uma nave", font=('Comic Sans MS', 12))
        self.lista = ttk.OptionMenu(self, self.opt, self.navesNomes[0], *self.navesNomes)
        self.buttonVoltar = ttk.Button(self, text="Voltar", command=self.showMain)
        self.button = ttk.Button(self, text="Buscar", command=self.buscarNave)

    def getInfo(self):
        self.rows = self.registro.getAllNaves()
        self.navesNomes = list()
        if (len(self.rows) != 0):
            for item in self.rows:
                self.navesNomes.append(item[1])
            
            self.lista = ttk.OptionMenu(self, self.opt, self.navesNomes[0], *self.navesNomes)
            return True
        self.navesNomes = ['placeholder']
        return False
    
    def buscarNave(self):
        naveSelecionada = self.opt.get()
        naveId = 0
        for item in self.rows:
            if (item[1] == naveSelecionada):
                naveId = item[0]
            
        self.showDetalhes(naveId)

    def show(self):
        self.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor='center')

        # colocar na tela
        self.columnconfigure((0, 1), weight=1, uniform='a')
        self.rowconfigure((0, 1), weight=1, uniform='a')

        self.label.grid(row=0, column=0, padx=10, pady=20, sticky='nsew')
        self.lista.grid(row=0, column=1, padx=10, pady=20, sticky='nsew')
        self.buttonVoltar.grid(row=1, column=0, padx=10, pady=20, sticky='nsew')
        self.button.grid(row=1, column=1, padx=10, pady=20, sticky='nsew')
    
    def hide(self):
        self.label.grid_forget()
        self.lista.grid_forget()
        self.buttonVoltar.grid_forget()
        self.button.grid_forget()
        self.place_forget()