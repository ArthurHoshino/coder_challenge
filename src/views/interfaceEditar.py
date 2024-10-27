import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.classes.Registro import Registro
import logging

class InterfaceEditar(ttk.Frame):
    def __init__(self, parent, showListarNaves, showDetalhes):
        super().__init__(parent)
        self.showListarNaves = showListarNaves
        self.showDetalhes = showDetalhes
        self.registro = Registro()

        self.naveId = 0

        # opcoes para registro
        self.menuOpt = {}
        self.optSelecionado = {}
        self.optValue = {
            "nome": tk.StringVar(self),
            "tamanho": tk.StringVar(self),
            "cor": tk.StringVar(self),
            "local_queda": tk.StringVar(self),
            "poderio": tk.StringVar(self),
            "combustiveis": tk.StringVar(self),
            "qtdSobrevivente": tk.StringVar(self),
            "trip_estado": tk.StringVar(self),
            "avaria": tk.StringVar(self),
            "potencial": tk.StringVar(self),
            "periculosidade": tk.StringVar(self),
            "qtdInfo": tk.StringVar(self)
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
        self.armamento = tk.Listbox(self, selectmode="multiple", exportselection=0)
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

        self.qtdInfoLabel = ttk.Label(self, text="Quantidade de informações", font=('Comic Sans MS', 12))
        self.qtdInfo = ttk.OptionMenu(self, self.optValue['qtdInfo'], self.menuOpt['info'][0], *self.menuOpt['info'])

        self.buttonVoltar = ttk.Button(self, text="Voltar", command=self.showDetalhes)
        self.button = ttk.Button(self, text="Salvar", command=self.salvarAlteracao)
    
    def validate(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def salvarAlteracao(self):
        data = {}
        data['id'] = self.naveId
        data['nome'] = self.optValue['nome'].get()
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
        data['info'] = self.menuOpt['info'].index(self.optValue['qtdInfo'].get()) # int

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

        response = self.registro.editar(data)
        if (response == 200):
            messagebox.showinfo("Sucesso", "Nave atualizada com sucesso")
        else:
            messagebox.showerror("Ops!", "Algo deu errado =(")
        
        self.showListarNaves()
    
    def getInfo(self):
        with open("src/options.json", "r", encoding='utf-8') as f:
            self.menuOpt = json.load(f)
        
    def setInfo(self, naveId):
        # limpar os campos
        self.resetValues()
        self.naveId = naveId

        response = self.registro.getNaveById(self.naveId)

        # DEFINIR OS VALORES DAS VARIAVEIS DE CADA CAMPO
        self.optValue['nome'].set(response[1])
        self.optValue['tamanho'].set(self.menuOpt['tamanho'][response[2]])
        self.optValue['cor'].set(self.menuOpt['cor'][response[3]])
        self.optValue['local_queda'].set(self.menuOpt['local_queda'][self.menuOpt['local_queda'].index(response[4])])
        self.optValue['poderio'].set(self.menuOpt['poderio'][response[5] // 256])
        self.optValue['combustiveis'].set(self.menuOpt['combustiveis'][self.menuOpt['combustiveis'].index(response[6])])
        self.optValue['qtdSobrevivente'].set(response[7])
        self.optValue['trip_estado'].set(self.menuOpt['trip_estado'][self.menuOpt['trip_estado'].index(response[8])])
        self.optValue['avaria'].set(self.menuOpt['avaria'][response[9]])
        self.optValue['potencial'].set(self.menuOpt['potencial'][response[10]])
        self.optValue['periculosidade'].set(self.menuOpt['periculosidade'][response[11]])
        self.optValue['qtdInfo'].set(self.menuOpt['info'][response[12]])

        # DEFINIR OS VALORES DOS CAMPOS
        # self.nome.insert(0, response[1])
        self.tamanho.set_menu(self.menuOpt['tamanho'][response[2]], *self.menuOpt['tamanho'])
        self.cor.set_menu(self.menuOpt['cor'][response[3]], *self.menuOpt['cor'])
        self.local.set_menu(self.menuOpt['local_queda'][self.menuOpt['local_queda'].index(response[4])], *self.menuOpt['local_queda'])
        self.poder.set_menu(self.menuOpt['poderio'][response[5] // 256], *self.menuOpt['poderio'])

        # logica das armas selecionadas
        armasSelecionadas = format((response[5] % 256), 'b')[::-1]
        contador = 0
        for arma in armasSelecionadas:
            if (arma == '1'):
                self.armamento.select_set(contador)
            contador += 1

        self.combustivel.set_menu(self.menuOpt['combustiveis'][self.menuOpt['combustiveis'].index(response[6])], *self.menuOpt['combustiveis'])
        # self.qtdSobrevivente.insert(0, response[7])
        self.estadoSobrevivente.set_menu(self.menuOpt['trip_estado'][self.menuOpt['trip_estado'].index(response[8])], *self.menuOpt['trip_estado'])
        self.avaria.set_menu(self.menuOpt['avaria'][response[9]], *self.menuOpt['avaria'])
        self.potencial.set_menu(self.menuOpt['potencial'][response[10]], *self.menuOpt['potencial'])
        self.periculosidade.set_menu(self.menuOpt['periculosidade'][response[11]], *self.menuOpt['periculosidade'])
        self.qtdInfo.set_menu(self.menuOpt['info'][response[12]], *self.menuOpt['info'])
    
    def resetValues(self):
        self.nome.delete(0, tk.END)
        self.qtdSobrevivente.delete(0, tk.END)
        self.armamento.selection_clear(0, tk.END)

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

        self.qtdInfoLabel.grid(row=6, column=2, padx=10, pady=20, sticky='nsew')
        self.qtdInfo.grid(row=6, column=3, padx=10, pady=20, sticky='nsew')

        self.buttonVoltar.grid(row=7, column=0, padx=20, pady=20, sticky='nsew', columnspan=2)
        self.button.grid(row=7, column=2, padx=20, pady=20, sticky='nsew', columnspan=2)
    
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
        self.qtdInfoLabel.grid_forget()
        self.qtdInfo.grid_forget()
        self.button.grid_forget()
        self.buttonVoltar.grid_forget()
        self.place_forget()
