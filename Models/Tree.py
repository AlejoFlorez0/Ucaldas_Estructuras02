import os

class Tree:

    # Constructor ([listaNodosIniciales], [raiz])
    def __init__(self):
        self.Caves = []
        self.raiz = None
        self.peso = 0
        self.altura = 0
        self.loadData()

    #Cargará los peajes existentes
    def loadData(self):
        if os.path.exists("File/Cave"):
            contentPath = os.listdir("File/Cave")
            for file in contentPath:
                self.Caves.append(file)

        return True

    #Define un nodo como raiz
    def PonerRaiz(self, raiz):
        self.raiz = raiz

    #Obtiene el peso del arbol
    def ObtenerPeso(self):
        return self.peso

    # Pre-order (R-I-D)
    def imprimir_pre_order(self, nodo, isSon = "Raiz",isFather=0):
        if (nodo):
            print(isSon)
            print(isFather)
            print(f"- Peaje: {nodo.nombre} , - nombre: {nodo.nombre} , -valor: {nodo.valor}, -Recargo por Izquierda {nodo.ObtenerRecargoIz()}, -Recargo por Derecha {nodo.ObtenerRecargoDe()}, -Categoria {nodo.categoria}.")
            self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo(),"Izquierdo",nodo.valor)
            self.imprimir_pre_order(nodo.ObtenerHijoDerecho(),"Derecho",nodo.valor)