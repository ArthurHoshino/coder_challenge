import customtkinter, json

class InterfaceIndex:
    def __init__(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')
        self.root = customtkinter.CTk()
        self.root.geometry("1000x650")
        self.root.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.showFunctions = {
            "main": self.showMain,
            "registro": self.showRegistro
        }

        # opcoes para registro
        self.menuOpt = {}

        # main
        self.buttonRegistro = customtkinter.CTkButton(self.root, text="Registrar nave", command=self.showFunctions['registro'])
        self.buttonVisualizar = customtkinter.CTkButton(self.root, text="Visualizar naves")

        # registro
        self.tamanhoTitle = None
        self.tamanho = None
        self.corTitle = None
        self.cor = None
        self.localTitle = None
        self.local = None
        self.poderTitle = None
        self.poder = None
        self.armamentoTitle = None
        self.armamento = None
        self.combustivelTitle = None
        self.combustivel = None
        self.qtdSobreviventeTitle = None
        self.qtdSobrevivente = None
        self.estadoSobrevivente = None
        self.avariaTitle = None
        self.avaria = None
        self.potencialTitle = None
        self.potencial = None
        self.periculosidadeTitle = None
        self.periculosidade = None
        self.buttom = customtkinter.CTkButton(self.root, text="Enviar", command=self.registrar)
        self.buttomVoltar = customtkinter.CTkButton(self.root, text="Voltar", command=self.showFunctions['main'])

    def getOptions(self):
        with open("src/options.json", "r", encoding='utf-8') as f:
            self.menuOpt = json.load(f)

        self.tamanhoTitle = customtkinter.CTkLabel(self.root, text="Tamanho da nave", font=('Comic Sans MS', 14))
        self.tamanho = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['tamanho'])
        self.corTitle = customtkinter.CTkLabel(self.root, text="Cor da nave", font=('Comic Sans MS', 14))
        self.cor = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['cor'])
        self.localTitle = customtkinter.CTkLabel(self.root, text="Local da queda", font=('Comic Sans MS', 14))
        self.local = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['local_queda'])
        self.poderTitle = customtkinter.CTkLabel(self.root, text="Poderio bélico", font=('Comic Sans MS', 14))
        self.poder = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['poderio'])
        self.armamentoTitle = customtkinter.CTkLabel(self.root, text="Armamento", font=('Comic Sans MS', 14))
        self.armamento = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['armas'])
        self.combustivelTitle = customtkinter.CTkLabel(self.root, text="Combustível", font=('Comic Sans MS', 14))
        self.combustivel = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['combustiveis'])
        self.qtdSobreviventeTitle = customtkinter.CTkLabel(self.root, text="Número de sobreviventes", font=('Comic Sans MS', 14))
        self.qtdSobrevivente = customtkinter.CTkEntry(self.root)
        self.estadoSobreviventeTitle = customtkinter.CTkLabel(self.root, text="Estado dos sobreviventes", font=('Comic Sans MS', 14))
        self.estadoSobrevivente = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['trip_estado'])
        self.avariaTitle = customtkinter.CTkLabel(self.root, text="Grau de avaria", font=('Comic Sans MS', 14))
        self.avaria = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['avaria'])
        self.potencialTitle = customtkinter.CTkLabel(self.root, text="Potencial de prospecção tecnológica", font=('Comic Sans MS', 14))
        self.potencial = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['potencial'])
        self.periculosidadeTitle = customtkinter.CTkLabel(self.root, text="Grau de periculosidade", font=('Comic Sans MS', 14))
        self.periculosidade = customtkinter.CTkOptionMenu(self.root, values=self.menuOpt['periculosidade'])

    def hide_all(self):
        self.hideMain()
        self.hideRegistro()
    
    def registrar(self):
        print(self.options.get())
    
    # show functions
    def showMain(self):
        self.hide_all()
        self.buttonRegistro.pack(padx=20, pady=12)
        self.buttonVisualizar.pack(padx=20, pady=12)

    def showRegistro(self):
        self.hide_all()

        self.tamanhoTitle.grid(row=0, column=0, padx=10, pady=20, sticky='ew')
        self.tamanho.grid(row=0, column=1, padx=10, pady=20, sticky='ew')
        self.corTitle.grid(row=1, column=0, padx=10, pady=20, sticky='ew')
        self.cor.grid(row=1, column=1, padx=10, pady=20, sticky='ew')
        self.localTitle.grid(row=2, column=0, padx=10, pady=20, sticky='ew')
        self.local.grid(row=2, column=1, padx=10, pady=20, sticky='ew')
        self.poderTitle.grid(row=3, column=0, padx=10, pady=20, sticky='ew')
        self.poder.grid(row=3, column=1, padx=10, pady=20, sticky='ew')
        self.armamentoTitle.grid(row=4, column=0, padx=10, pady=20, sticky='ew')
        self.armamento.grid(row=4, column=1, padx=10, pady=20, sticky='ew')
        self.combustivelTitle.grid(row=5, column=0, padx=10, pady=20, sticky='ew')
        self.combustivel.grid(row=5, column=1, padx=10, pady=20, sticky='ew')
        self.qtdSobreviventeTitle.grid(row=0, column=2, padx=10, pady=20, sticky='ew')
        self.qtdSobrevivente.grid(row=0, column=3, padx=10, pady=20, sticky='ew')
        self.estadoSobreviventeTitle.grid(row=1, column=2, padx=10, pady=20, sticky='ew')
        self.estadoSobrevivente.grid(row=1, column=3, padx=10, pady=20, sticky='ew')
        self.avariaTitle.grid(row=2, column=2, padx=10, pady=20, sticky='ew')
        self.avaria.grid(row=2, column=3, padx=10, pady=20, sticky='ew')
        self.potencialTitle.grid(row=3, column=2, padx=10, pady=20, sticky='ew')
        self.potencial.grid(row=3, column=3, padx=10, pady=20, sticky='ew')
        self.periculosidadeTitle.grid(row=4, column=2, padx=10, pady=20, sticky='ew')
        self.periculosidade.grid(row=4, column=3, padx=10, pady=20, sticky='ew')

        self.buttom.grid(row=11, column=0, padx=20, pady=20, sticky='w', columnspan=2)
        self.buttomVoltar.grid(row=11, column=2, padx=20, pady=20, sticky='w', columnspan=2)

    # hide functions
    def hideMain(self):
        self.buttonRegistro.pack_forget()
        self.buttonVisualizar.pack_forget()

    def hideRegistro(self):
        self.tamanhoTitle.grid_forget()
        self.tamanho.grid_forget()
        self.corTitle.grid_forget()
        self.cor.grid_forget()
        self.localTitle.grid_forget()
        self.local.grid_forget()
        self.poderTitle.grid_forget()
        self.poder.grid_forget()
        self.armamentoTitle.grid_forget()
        self.armamento.grid_forget()
        self.combustivelTitle.grid_forget()
        self.combustivel.grid_forget()
        self.qtdSobreviventeTitle.grid_forget()
        self.qtdSobrevivente.grid_forget()
        self.estadoSobreviventeTitle.grid_forget()
        self.estadoSobrevivente.grid_forget()
        self.avariaTitle.grid_forget()
        self.avaria.grid_forget()
        self.potencialTitle.grid_forget()
        self.potencial.grid_forget()
        self.periculosidadeTitle.grid_forget()
        self.periculosidade.grid_forget()
        self.buttom.grid_forget()
        self.buttomVoltar.grid_forget()

    def run(self):
        self.getOptions()
        self.showMain()
        self.root.mainloop()

    
    
    
    
    
