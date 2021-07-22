import json
import tkinter

from tkinter import *
from Models.Cave import Cave

class send:

    def __init__(self,Tree):
        
        self.Tree = Tree
        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Montaña ACME - Alejandro González - Marlon Herrera - Bryan Mauricio González")

        self.valueOrigin = tkinter.StringVar(self.windows)
        self.valueOrigin.set("Selecciona una opción")

        self.valueDestination = tkinter.StringVar(self.windows)
        self.valueDestination.set("Selecciona una opción")

        # Define los enlaces de origen
        self.links = OptionMenu(self.windows,self.valueOrigin,*self.Tree.Caves)

        # Define los enlaces de destino
        self.links = OptionMenu(self.windows,self.valueDestination,*self.Tree.Caves)

    
    def show(self):

        self.linksOrigin = OptionMenu(self.windows,self.valueOrigin,*self.Tree.Caves)
        self.linksOrigin.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.1)

        self.linksDestination = OptionMenu(self.windows,self.valueDestination,*self.Tree.Caves)
        self.linksDestination.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)

        btnSave = Button(self.windows,text="Guardar",relief="groove",cursor="hand2",command=self.__save)
        btnSave.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnSave.place(relx=0.35,rely=0.8, relwidth=0.3, relheight=0.1)


    def __save(self):

        jsonFile = {'origin': self.valueOrigin.get(), 'destination': self.valueDestination.get()}

        with open("File//Send//send.json",'w') as json_file:
            json.dump(jsonFile, json_file)