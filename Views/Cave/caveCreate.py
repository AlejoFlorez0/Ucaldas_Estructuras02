import tkinter

from tkinter import *
from Models.Cave import Cave

class caveCreate:

    def __init__(self,Tree,Cave = None):

        self.Tree = Tree
        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Montaña ACME - Alejandro González - Marlon Herrera - Bryan Mauricio González")

        # Define el valor del nombre
        self.nameValue = Entry(self.windows)

        # Define la posición en X
        self.xPosition = Entry(self.windows)

        # Define la posición en Y
        self.yPosition = Entry(self.windows)

        if Cave:
            self.load(Cave)

    # Cargará los registros de otro
    def load(self,Cave):
        pass
        

    #Mostrar interfaz grafica
    def show(self):

        title = Label(self.windows, text="Montaña ACME - Agregar Cueva")
        title.config(bg="#C861D3", fg="white", font=("Comic Sans", 16))
        title.place(x=0,y=0,relwidth=1,relheight=0.1)

        nameLabel = Label(self.windows ,text = "Nombre",borderwidth=2, relief="groove")
        nameLabel.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        nameLabel.place(relx=0,rely=0.1,relwidth=0.5,relheight=0.1)

        self.nameValue = Entry(self.windows,textvariable=self.nameValue)
        self.nameValue.place(relx=0.5,rely=0.1,relwidth=0.5,relheight=0.1)

        xPositionLabel = Label(self.windows ,text = "Posición X",borderwidth=2, relief="groove")
        xPositionLabel.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        xPositionLabel.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.1)

        self.xPosition = Entry(self.windows,textvariable=self.xPosition)
        self.xPosition.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)

        yPositionLabel = Label(self.windows ,text = "Posición Y",borderwidth=2, relief="groove")
        yPositionLabel.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        yPositionLabel.place(relx=0,rely=0.3,relwidth=0.5,relheight=0.1)

        self.yPosition = Entry(self.windows,textvariable=self.yPosition)
        self.yPosition.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.1)


        btnSave = Button(self.windows,text="Guardar",relief="groove",cursor="hand2",command=self.__save)
        btnSave.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnSave.place(relx=0.35,rely=0.8, relwidth=0.3, relheight=0.1)

        self.windows.mainloop()

    # Creará una instancia de la clase Cave
    def __save(self):
        
        instaceCave = Cave(self.Tree)
        instaceCave.setName(self.nameValue.get())
        instaceCave.setXPosition(self.xPosition.get())
        instaceCave.setYPosition(self.yPosition.get())
        
        if instaceCave.save():
            self.windows.destroy()
