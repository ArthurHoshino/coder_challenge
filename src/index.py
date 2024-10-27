import tkinter as tk
from tkinter import messagebox

# Views
from src.views.interfaceMain import InterfaceMain
from src.views.interfaceRegistro import InterfaceRegistro
from src.views.interfaceListarNaves import InterfaceListarNaves
from src.views.interfaceDetalhes import InterfaceDetalhes
from src.views.interfaceEditar import InterfaceEditar

class InterfaceIndex(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1250x750")
        self.minsize(1200, 700)

        self.appRunning = False

        # views
        self.interface_main = InterfaceMain(self, self.show_registro, self.show_listar_naves)
        self.interface_registro = InterfaceRegistro(self, self.show_main)
        self.interface_listar_naves = InterfaceListarNaves(self, self.show_main, self.show_detalhes)
        self.interface_detalhes = InterfaceDetalhes(self, self.show_main, self.show_listar_naves, self.show_editar)
        self.interface_editar = InterfaceEditar(self, self.show_listar_naves, self.show_detalhes)

        # chamada
        self.show_main()
        self.mainloop()
    
    def hide_all(self):
        self.interface_main.hide()
        self.interface_registro.hide()
        self.interface_listar_naves.hide()
        self.interface_detalhes.hide()
        self.interface_editar.hide()
        
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
        response = self.interface_listar_naves.getInfo()
        if (response):
            self.hide_all()
            self.interface_listar_naves.show()
        else:
            messagebox.showwarning("warning", 'Sem naves registradas')
        
    def show_detalhes(self, naveId: int = 0):
        self.interface_detalhes.setInfo(naveId=naveId)
        self.hide_all()
        self.interface_detalhes.show()
    
    def show_editar(self, naveId):
        self.interface_editar.setInfo(naveId=naveId)
        self.hide_all()
        self.interface_editar.show()
