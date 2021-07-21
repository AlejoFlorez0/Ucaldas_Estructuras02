import tkinter

from tkinter import *
from Models.Cave import Cave

class caveCreate:

    def __init__(self,Tree,CaveId = None):

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

        #Valor de la lista de json
        self.value_inside = tkinter.StringVar(self.windows)
        self.value_inside.set("Selecciona una opción")

        # Valor de todos los bloques seleccionados por usuario
        self.selectedLinks = []

        # Define los enlaces 
        self.links = OptionMenu(self.windows,self.value_inside,*self.Tree.Caves)

        self.containerList = Frame(self.windows)

        if CaveId is not None:
            self.entryNameValue = tkinter.StringVar()
            self.entryXPosition = tkinter.StringVar()
            self.entryYPosition = tkinter.StringVar()
            
            self.Cave = Cave(self.Tree)
            self.Cave.loadFromFile(CaveId+".json")
        
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

        linksLabel = Label(self.windows ,text = "Enlaces",borderwidth=2, relief="groove")
        linksLabel.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        linksLabel.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.1)

        self.links = OptionMenu(self.windows,self.value_inside,*self.Tree.Caves)
        self.links.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.1)

        btnAddLink = Button(self.windows,text="Agregar Enlace",relief="groove",cursor="hand2",command=self.__addLink)
        btnAddLink.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnAddLink.place(relx=0,rely=0.5, relwidth=1, relheight=0.1)

        self.containerList.place(relwidth=1,relheight=0.3,rely=0.6,relx=0)

        btnSave = Button(self.windows,text="Guardar",relief="groove",cursor="hand2",command=self.__save)
        btnSave.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnSave.place(relx=0.35,rely=0.8, relwidth=0.3, relheight=0.1)

        self.windows.mainloop()

    # Abrirá el formulario especial para la actualización de archivo
    def update(self):
        
        title = Label(self.windows, text="Montaña ACME - Actualizar Cueva "+self.Cave.getName())
        title.config(bg="#C861D3", fg="white", font=("Comic Sans", 16))
        title.place(x=0,y=0,relwidth=1,relheight=0.1)

        nameLabel = Label(self.windows ,text = "Nombre",borderwidth=2, relief="groove")
        nameLabel.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        nameLabel.place(relx=0,rely=0.1,relwidth=0.5,relheight=0.1)

        self.nameValue = Entry(self.windows,textvariable=self.entryNameValue)
        self.nameValue.place(relx=0.5,rely=0.1,relwidth=0.5,relheight=0.1)
        self.entryNameValue.set(self.Cave.getName())

        xPositionLabel = Label(self.windows ,text = "Posición X",borderwidth=2, relief="groove")
        xPositionLabel.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        xPositionLabel.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.1)

        self.xPosition = Entry(self.windows,textvariable=self.entryXPosition)
        self.xPosition.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)
        self.entryXPosition.set(self.Cave.getXPosition())

        yPositionLabel = Label(self.windows ,text = "Posición Y",borderwidth=2, relief="groove")
        yPositionLabel.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        yPositionLabel.place(relx=0,rely=0.3,relwidth=0.5,relheight=0.1)

        self.yPosition = Entry(self.windows,textvariable=self.entryYPosition)
        self.yPosition.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.1)
        self.entryYPosition.set(self.Cave.getYPosition())

        btnUpdate = Button(self.windows,text="Actualizar",relief="groove",cursor="hand2",command=self.__update)
        btnUpdate.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnUpdate.place(relx=0.35,rely=0.8, relwidth=0.3, relheight=0.1)

        self.windows.mainloop()

        return True

    # Agregará el valor seleccionado
    def __addLink(self):
        self.selectedLinks.append(self.value_inside.get())
        checkbox = Checkbutton(self.containerList, text=self.value_inside.get())
        checkbox.pack()


    # Creará una instancia de la clase Cave
    def __save(self):
        
        instaceCave = Cave(self.Tree)
        instaceCave.setName(self.nameValue.get())
        instaceCave.setXPosition(self.xPosition.get())
        instaceCave.setYPosition(self.yPosition.get())
        instaceCave.setLinks(self.selectedLinks)

        if instaceCave.save():
            self.windows.destroy()

    # Actualizará una instancia de la clase Cave
    def __update(self):
        
        if self.Cave.update():
            self.windows.destroy()
