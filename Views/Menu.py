import os
import tkinter
from tkinter import Frame
from Models.Cave import Cave
from Views.Tree.treeNode import treeNode
from Views.Cave.caveCreate import caveCreate

class Menu:

    def __init__(self,Tree):

        self.Tree = Tree
        self.windows = tkinter.Tk()
        self.windows.geometry("900x500")
        self.windows.title("Montaña ACME - Alejandro González - Marlon Herrera - Bryan Mauricio González")
        
        self.__config()

    # Configuración inicial de la cuevas
    # Creará las cuevas ya configuradas
    def __config(self):

        frame = Frame(self.windows)
        frame.config(height=700,bg="red")
        frame.pack(fill="x",pady=75)

        if os.path.exists("File/Cave"):
            contentPath = os.listdir("File/Cave")
            for file in contentPath:
                instanceCave = Cave()
                instanceCave.loadFromFile(file)

                # Crea un boton que simulará ser la cueva en la posición guardadá en json
                btnCave = tkinter.Button(frame, text=instanceCave.getName(),command=self.__Cave)
                btnCave.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
                btnCave.place(relx=instanceCave.getXPosition(),rely=instanceCave.getYPosition(), relwidth=0.1, relheight=0.1)
        pass

    # Mostrará un nuevo
    def show(self):

        btnCave = tkinter.Button(self.windows, text="Agregar Cuevas",command=self.__Cave)
        btnCave.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnCave.place(relx=0.8,rely=0, relwidth=0.2, relheight=0.15)

        #btnTree = tkinter.Button(self.windows, text="Arbol",command=self.__Tree)
        #btnTree.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        #btnTree.place(relx=0.7,rely=0.25, relwidth=0.25, relheight=0.3)

        self.windows.mainloop()

    # Abrirá el Formulario para la creación de la cueva
    def __Cave(self):
        instanceTollIndex = caveCreate(self.Tree)
        instanceTollIndex.show()

    # Abrirá el Formulario para el arbol
    def __Tree(self):
        instanceTreeIndex = treeNode(self.Tree.raiz)
        self.windows.destroy()
        instanceTreeIndex.show()
