import tkinter as tk
from tkinter import ttk

class InterfaceMain(ttk.Frame):
    def __init__(self, parent, showRegistro):
        super().__init__(parent)
        self.showRegistro = showRegistro

        self.buttonRegistro = None
        self.buttonVisualizar = None

    def show(self):
        # criar componentes
        self.place( relx=0.5, rely=0.2, relwidth=0.5, relheight=0.2, anchor='center' )
        self.buttonRegistro = ttk.Button(self, text="Registrar nave", command=self.showRegistro)
        self.buttonVisualizar = ttk.Button(self, text="Visualizar naves")

        # colocar na tela
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')

        self.buttonRegistro.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.buttonVisualizar.grid(row=0, column=2, columnspan=2, sticky='nsew')

    def hide(self):
        self.buttonRegistro.grid_forget()
        self.buttonVisualizar.grid_forget()
        self.place_forget()
        
        