import os
import tkinter

from Views.Menu import Menu
from Models.Tree import Tree

class index:

    def __init__(self):
        
        self.Tree = Tree()
        self.windows = tkinter.Tk()
        self.windows.geometry("500x300")
        self.windows.title("Montaña ACME - Alejandro González - Marlon Herrera - Bryan Mauricio González")

        self.config()

    # Validará sí ya existe un archivo de carga de archivos
    # En caso de que exista hará una pregunta de validación
    # Caso contrarío abrirá la interfaz inicial
    def config(self):
        if(os.path.exists("File/Cave")):
            self.toBeContinue()
        else:
            instanceMenu = Menu(self.Tree)
            self.windows.destroy()
            instanceMenu.show()

    # Interfaz gráfica al iniciar
    def toBeContinue(self):

        label1 = tkinter.Label(self.windows, text="Montaña ACME\n ¿Desea Continuar con la configuración actual?")
        label1.config(bg="#56d187", fg="white", font=("Comic Sans", 16))
        label1.place(x=0,y=0,relwidth=1,relheight=0.2)

        btn = tkinter.Button(self.windows, text="Si", command=self.isSuccess)
        btn.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btn.place(relx=0.05,rely=0.5, relwidth=0.3, relheight=0.15)

        btn = tkinter.Button(self.windows, text="No", command=self.cancelledSystem)
        btn.config(bg="#d9534f", fg="white", font=("Comic Sans", 18))
        btn.place(relx=0.65,rely=0.5, relwidth=0.3, relheight=0.15)

        self.windows.mainloop()

    # Función cuando desea continuar con el sistema anterior
    def isSuccess(self):
        instanceMenu = Menu(self.Tree)
        self.windows.destroy()
        instanceMenu.show()

    # Cerrará la isntancia actual del sistema
    def cancelledSystem(self):
        self.windows.destroy()

instance = index()
