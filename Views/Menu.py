import os
import json
import tkinter
from tkinter import Frame
from tkinter import Canvas
from tkinter.constants import Y
from Models.Cave import Cave
from Views.Cave.send import send
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
        frame.config(height=500,bg="red")
        frame.pack(fill="x")

        self.canvas = Canvas(frame,width=400, height=300)
        self.canvas.place(x=0,y=0,relwidth=1,relheight=1)

        if os.path.exists("File/Cave"):
            contentPath = os.listdir("File/Cave")

            self.__createLine(contentPath)

            for file in contentPath:
                instanceCave = Cave()
                instanceCave.loadFromFile(file)

                # Crea un boton que simulará ser la cueva en la posición guardadá en json
                btnCave = tkinter.Button(frame, text=instanceCave.getName(),command=lambda:self.__caveUpdate(instanceCave.getName()))
                btnCave.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
                btnCave.place(relx=instanceCave.getXPosition(),rely=instanceCave.getYPosition(), relwidth=0.1, relheight=0.1)

        return True

    # Mostrará un nuevo
    def show(self):

        self.showTravel()

        btnCave = tkinter.Button(self.windows, text="Agregar Cuevas",command=self.__Cave)
        btnCave.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnCave.place(relx=0.8,rely=0, relwidth=0.2, relheight=0.15)

        btnTree = tkinter.Button(self.windows, text="Recorrido",command=self.__Tree)
        btnTree.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnTree.place(relx=0.85,rely=0.15, relwidth=0.15, relheight=0.15)

        self.windows.mainloop()


    def showTravel(self):
        file = open ("File//Send//send.json", "r")
        data = json.loads(file.read())

        origin = data["origin"]
        destination = data["destination"]

        

    # Abrirá el formulario de actualización de registros
    def __caveUpdate(self,instanceName):
        
        instanceCave = caveCreate(self.Tree,instanceName)
        instanceCave.update()
        return True

    # Abrirá el Formulario para la creación de la cueva
    def __Cave(self):
        instanceTollIndex = caveCreate(self.Tree)
        instanceTollIndex.show()

    # Abrirá el Formulario para el arbol
    def __Tree(self):
        instanceTreeIndex = send(self.Tree)
        instanceTreeIndex.show()

    # Se crea linea dinamica entre varias cuevas
    def __createLine(self,contentPath):
        
        for file in contentPath:
            instanceCave = Cave()
            instanceCave.loadFromFile(file)

            for link in instanceCave.GetLinks(): 
                data = json.loads(json.dumps(link))
                caveLink = Cave()
                caveLink.loadFromFile(data["Cave"])
                if(data["state"]):
                    self.canvas.create_line((instanceCave.getXPosition() * 900),(instanceCave.getYPosition() * 500), (caveLink.getXPosition() * 900), (caveLink.getYPosition() * 500),arrow="last")
                else:
                    self.canvas.create_line((instanceCave.getXPosition() * 900),(instanceCave.getYPosition() * 500), (caveLink.getXPosition() * 900), ((caveLink.getYPosition() * 500)),arrow='last',dash=(5, 3))

        return True