import tkinter as tk

# Views
from src.views.interfaceMain import InterfaceMain
from src.views.interfaceRegistro import InterfaceRegistro

class InterfaceIndex(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1250x650")
        self.minsize(1200, 650)

        self.appRunning = False

        # views
        self.interface_main = InterfaceMain(self, self.show_registro)
        self.interface_registro = InterfaceRegistro(self, self.show_main)

        # chamada
        self.show_main()
        self.mainloop()
        
    def show_main(self):
        if self.appRunning:
            self.interface_registro.hide()
        else:
            self.appRunning = True
        self.interface_main.show()
    
    def show_registro(self):
        self.interface_main.hide()
        self.interface_registro.show()
