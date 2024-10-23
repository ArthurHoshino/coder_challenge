import tkinter as tk
from tkinter import messagebox

# Views
from src.views.interfaceMain import InterfaceMain
from src.views.interfaceRegistro import InterfaceRegistro
from src.views.interfaceListarNaves import InterfaceListarNaves

class InterfaceIndex(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1250x650")
        self.minsize(1200, 650)

        self.appRunning = False

        # views
        self.interface_main = InterfaceMain(self, self.show_registro, self.show_listar_naves)
        self.interface_registro = InterfaceRegistro(self, self.show_main)
        self.interface_listar_naves = InterfaceListarNaves(self, self.show_main)

        # chamada
        self.show_main()
        self.mainloop()
    
    def hide_all(self):
        self.interface_main.hide()
        self.interface_registro.hide()
        self.interface_listar_naves.hide()
        
    def show_main(self):
        if self.appRunning:
            self.hide_all()
        else:
            self.appRunning = True
        self.interface_main.show()
    
    def show_registro(self):
        self.hide_all()
        self.interface_registro.show()

    def show_listar_naves(self):
        self.interface_listar_naves.getInfo()
        if (self.interface_listar_naves.navesNomes[0] == 'Placeholder'):
            messagebox.showwarning("warning", 'Sem naves registradas')
        else:
            self.hide_all()
            self.interface_listar_naves.show()
