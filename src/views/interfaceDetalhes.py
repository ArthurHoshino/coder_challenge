import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.classes.Registro import Registro

class InterfaceDetalhes(ttk.Frame):
    def __init__(self, parent, showMain, showListarNaves, showEditar):
        super().__init__(parent)
        self.showMain = showMain
        self.showListarNaves = showListarNaves
        self.showEditar = showEditar
        self.registro = Registro()

        self.toggle = True
        self.naveId = 0

        # opcoes para registro
        self.menuOpt = {}
        self.armasOpt = []

        self.getInfo()

        # registro
        self.nomeLabel = ttk.Label(self, text="Nome da nave", font=('Comic Sans MS', 12))
        self.nome = ttk.Entry(self)
        self.tamanhoLabel = ttk.Label(self, text="Tamanho da nave", font=('Comic Sans MS', 12))
        self.tamanho = ttk.Entry(self)
        self.corLabel = ttk.Label(self, text="Cor da nave", font=('Comic Sans MS', 12))
        self.cor = ttk.Entry(self)
        self.localLabel = ttk.Label(self, text="Local da queda", font=('Comic Sans MS', 12))
        self.local = ttk.Entry(self)
        self.poderLabel = ttk.Label(self, text="Poderio bélico", font=('Comic Sans MS', 12))
        self.poder = ttk.Entry(self)
        self.armamentoLabel = ttk.Label(self, text="Armamento", font=('Comic Sans MS', 12))
        self.armamento = tk.Listbox(self)
        self.combustivelLabel = ttk.Label(self, text="Combustível", font=('Comic Sans MS', 12))
        self.combustivel = ttk.Entry(self)
        self.qtdSobreviventeLabel = ttk.Label(self, text="Número de sobreviventes", font=('Comic Sans MS', 12))
        self.qtdSobrevivente = ttk.Entry(self)
        self.estadoSobreviventeLabel = ttk.Label(self, text="Estado dos sobreviventes", font=('Comic Sans MS', 12))
        self.estadoSobrevivente = ttk.Entry(self)
        self.avariaLabel = ttk.Label(self, text="Grau de avaria", font=('Comic Sans MS', 12))
        self.avaria = ttk.Entry(self)
        self.potencialLabel = ttk.Label(self, text="Potencial de prospecção tecnológica", font=('Comic Sans MS', 12))
        self.potencial = ttk.Entry(self)
        self.periculosidadeLabel = ttk.Label(self, text="Grau de periculosidade", font=('Comic Sans MS', 12))
        self.periculosidade = ttk.Entry(self)
        self.classificacaoLabel = ttk.Label(self, text="Classificação", font=('Comic Sans MS', 12))
        self.classificacao = ttk.Entry(self)
        self.qtdInfoLabel = ttk.Label(self, text="Informações armazenadas", font=('Comic Sans MS', 12))
        self.qtdInfo = ttk.Entry(self)

        self.buttonVoltar = ttk.Button(self, text="Voltar", command=self.showListarNaves)
        self.button = ttk.Button(self, text="Editar Informações", command=self.buscarNave)
        self.buttonDeletar = ttk.Button(self, text='Deletar Registro', command=self.deletarNave)

    def deletarNave(self):
        resposta = messagebox.askyesno(title='ATENÇÃO', message='Tem certeza de que deseja excluir esse registro?')
        if (resposta):
            response = self.registro.deletar(self.naveId)
            if response == 200:
                messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
                verify = self.registro.getAllNaves()
                if (len(verify) == 0):
                    self.showMain()
                else:
                    self.showListarNaves()
            else:
                messagebox.showerror("Ops!", "Algo deu errado =(")

    def toggleItems(self):
        estado = 'disable' if self.toggle else 'normal'
        self.nome.configure(state=estado)
        self.tamanho.configure(state=estado)
        self.cor.configure(state=estado)
        self.local.configure(state=estado)
        self.poder.configure(state=estado)
        self.armamento.configure(state=estado)
        self.combustivel.configure(state=estado)
        self.qtdSobrevivente.configure(state=estado)
        self.estadoSobrevivente.configure(state=estado)
        self.avaria.configure(state=estado)
        self.potencial.configure(state=estado)
        self.periculosidade.configure(state=estado)
        self.classificacao.configure(state=estado)
        self.qtdInfo.configure(state=estado)

        self.toggle = True
    
    def buscarNave(self):
        self.showEditar(self.naveId)
    
    def getInfo(self):
        with open("src/options.json", "r", encoding='utf-8') as f:
            self.menuOpt = json.load(f)
    
    def setInfo(self, naveId: int = 0):
        # habilitar os campos
        if (naveId != 0):
            self.naveId = naveId
        self.toggle = False
        self.toggleItems()

        # limpar os campos
        self.resetValues()

        response = self.registro.getNaveById(self.naveId)

        self.nome.insert(0, response[1])
        self.tamanho.insert(0, self.menuOpt['tamanho'][response[2]])
        self.cor.insert(0, self.menuOpt['cor'][response[3]])
        self.local.insert(0, response[4])
        self.poder.insert(0,  self.menuOpt['poderio'][ response[5] // 256 ] )

        # logica das armas selecionadas
        armasSelecionadas = format((response[5] % 256), 'b')[::-1]
        contador = 0
        for arma in armasSelecionadas:
            if (arma == '1'):
                self.armasOpt.append(self.menuOpt['armas'][contador])
            contador += 1
        for item in self.armasOpt:
            self.armamento.insert(self.armasOpt.index(item), item)

        self.combustivel.insert(0, response[6])
        self.qtdSobrevivente.insert(0, response[7])
        self.estadoSobrevivente.insert(0, response[8])
        self.avaria.insert(0, self.menuOpt['avaria'][response[9]])
        self.potencial.insert(0, self.menuOpt['potencial'][response[10]])
        self.periculosidade.insert(0, self.menuOpt['periculosidade'][response[11]])
        self.qtdInfo.insert(0, self.menuOpt['info'][response[12]])
        self.classificacao.insert(0, response[13])

        # desabilitar campos
        self.toggleItems()
    
    def resetValues(self):
        self.nome.delete(0, tk.END)
        self.tamanho.delete(0, tk.END)
        self.cor.delete(0, tk.END)
        self.local.delete(0, tk.END)
        self.poder.delete(0, tk.END)
        self.armamento.delete(0, tk.END)
        self.armasOpt = []
        self.combustivel.delete(0, tk.END)
        self.qtdSobrevivente.delete(0, tk.END)
        self.estadoSobrevivente.delete(0, tk.END)
        self.avaria.delete(0, tk.END)
        self.potencial.delete(0, tk.END)
        self.periculosidade.delete(0, tk.END)
        self.qtdInfo.delete(0, tk.END)
        self.classificacao.delete(0, tk.END)

    def show(self):
        self.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.95, anchor='center')
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, uniform='a')

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
        self.classificacaoLabel.grid(row=7, column=0, padx=10, pady=20, sticky='nsew')
        self.classificacao.grid(row=7, column=1, padx=10, pady=20, sticky='nsew')

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
        self.qtdInfoLabel.grid(row=6, column=2, padx=10, pady=20, sticky='nsew')
        self.qtdInfo.grid(row=6, column=3, padx=10, pady=20, sticky='nsew')

        self.buttonVoltar.grid(row=8, column=0, padx=20, pady=20, sticky='nsew')
        self.button.grid(row=8, column=1, padx=20, pady=20, sticky='nsew', columnspan=2)
        self.buttonDeletar.grid(row=8, column=3, padx=20, pady=20, sticky='nsew')
    
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
        self.classificacaoLabel.grid_forget()
        self.classificacao.grid_forget()
        self.qtdInfoLabel.grid_forget()
        self.qtdInfo.grid_forget()
        self.button.grid_forget()
        self.buttonVoltar.grid_forget()
        self.buttonDeletar.grid_forget()
        self.place_forget()
