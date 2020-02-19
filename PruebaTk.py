from TKinter import *

class iterfaz:
    def __init__(self, contenedor):
        self.el = Label(contenedor, texto = "Texto para ver Pruebas", fg="black", bg="white")
        self.el.pack()
    
ventana = Tk()
miInterfaz = interfaz(ventana)
