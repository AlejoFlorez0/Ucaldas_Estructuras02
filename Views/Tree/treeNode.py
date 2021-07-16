
import tkinter

class treeNode:

    def __init__(self,Node):
        self.Node = Node
        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Peajes Dora - Alejandro González Flórez - Marlon Aristizabal Herrea")
        self.__config()

    # Configuración de la vista principal
    def __config(self):
        return True

    # Mostrará la interfaz gráfica
    def show(self):

        title = tkinter.Label(self.windows, text="Peajes DORA")
        title.config(bg="#C861D3", fg="white", font=("Comic Sans", 18))
        title.place(x=0,y=0,relwidth=1,relheight=0.2)

        btnPeaje = tkinter.Label(self.windows, text=self.Node.nombre+"\n Valor: "+str(self.Node.valor))
        btnPeaje.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnPeaje.place(relx=0.35,rely=0.25, relwidth=0.3, relheight=0.3)

        if self.Node.ObtenerHijoIzquierdo():

            nodeLeft = self.Node.ObtenerHijoIzquierdo()

            nodeLeftText = nodeLeft.nombre+"\n Valor: "+str(nodeLeft.valor)+"\n HIJOS: \n"

            if nodeLeft.ObtenerHijoIzquierdo():
                nodeLeftText = nodeLeftText+"\n"+str(nodeLeft.ObtenerHijoIzquierdo().valor)+" <-"
            else:
                nodeLeftText = nodeLeftText+"\n"

            if nodeLeft.ObtenerHijoDerecho():           
                nodeLeftText = nodeLeftText+"-> "+str(nodeLeft.ObtenerHijoDerecho().valor)

            btnleftNode = tkinter.Button(self.windows, text=nodeLeftText,command=lambda: self.__showNode(nodeLeft))
            btnleftNode.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
            btnleftNode.place(relx=0,rely=0.6, relwidth=0.4, relheight=0.3)

        if self.Node.ObtenerHijoDerecho():

            nodeRight = self.Node.ObtenerHijoDerecho()

            nodeRightText = nodeRight.nombre+"\n Valor: "+str(nodeRight.valor)+"\n HIJOS: \n"

            if nodeRight.ObtenerHijoIzquierdo():
                nodeRightText = nodeRightText+"\n"+str(nodeRight.ObtenerHijoIzquierdo().valor)+" <-"
            else:
                nodeRightText = nodeRightText+"\n"

            if nodeRight.ObtenerHijoDerecho():           
                nodeRightText = nodeRightText+"-> "+str(nodeRight.ObtenerHijoDerecho().valor)

            btnRightNode = tkinter.Button(self.windows, text=nodeRightText,command=lambda: self.__showNode(nodeRight))
            btnRightNode.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
            btnRightNode.place(relx=0.6,rely=0.6, relwidth=0.4, relheight=0.3)

        self.windows.mainloop()

    #
    def __showNode(self,node):
        instenceNode = treeNode(node)
        instenceNode.show()
        return True
    