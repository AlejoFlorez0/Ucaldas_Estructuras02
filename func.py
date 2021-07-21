class Cave:
    
    def __init__(self, name):
        self.name = name
        self.links = {}
        self.supplies =[]

    def AddLinks(self, destination, distance,state):
        distances=[]
        if destination in self.links:
            distances=self.links[destination]
        distances.append({"Distancia":distance,"Estado":state})
        self.links[destination]=distances

    def GetName(self):
        return self.name

    def GetLink(self, name):
        for x in self.links:
            if name == x.GetName():

                return x
            return None

    def GetLinks(self):
        return self.links

    def PrintLinks(self):
        for x in self.links:
            for y in self.links[x]:
                dis=y["Distancia"]
                if y["Estado"] == False: st="CERRADO"
                else: st="ABIERTO"
                print(f"Enlace hacia {x.GetName()}, DISTANCIA : {dis} Metros, Estado:",st)

    def ChangeStatusLinks(self, destination):
        m= int(input("Distancia del enlace que desea cambiar: "))
        ListLinks=self.links[destination]
        for x in ListLinks:
            if x["Distancia"]==m:
                if x["Estado"]==False:
                    x["Estado"]=True
                else:
                    x["Estado"] = False

    def ChangeLinkDirecction(self, destination):
        m = int(input("Distancia del enlace que desea cambiar: "))
        ListLinks = self.links[destination]
        newLink=[]
        for x in self.links:
            for y in ListLinks:
                if y["Distancia"]==m:
                    newLink.append(self)
                    newLink.append(y["Distancia"])
                    newLink.append(y["Estado"])
                    del self.links[x]
                    return newLink
                return None


# Las funciones del grafo
# Montaña
class Graph:
    def __init__(self):
        self.Caves = {}

    # agregar Cueva
    def AddCave(self, name):
        c=Cave(name)
        entry=input("Desea colocar un id?: ")
        if "s" in entry:
            entry=input("Por favor escriba el id de la cueva: ")
            self.Caves[c]=entry
        else:
            self.Caves[c]=None
        return c

    def GetCave(self, name):
        for x in self.Caves:
            if name == x.GetName():
                return x
        return None

    def PrintCaves(self):
        for x in self.Caves:
            print(f"Nombre de la cueva: {x.GetName()}, Id: {self.Caves[x]}, Enlaces de la cueva: {x.links}")

    # Obtiene las conecciones salientes y entrantes de una cueva
    def Grade(self):
        name = (input("Ingrese el nombre de la cueva: "))
        s = 0
        e = 0
        for x in self.Caves:
            for y in x.links:
                if x.GetName() == name:
                    s = s + 1
                else:
                    if y.GetName() == name:
                        e = e + 1
        print(f"El número de conexiones salientes de {name}: {s}")
        print(f"El número de conexiones entrantes de {name}: {e}")

    # Cuando una cueva es inaccesible
    def Inna(self, lista):
        for x in self.Caves:
            b = True
            name = x.GetName()
            for y in self.Caves:
                for z in y.links:
                    if z.GetName() == name:
                        b = False
            if b == True:
                lista.append(x)
        return lista


g= Graph()

m = False

while m==False:
    print("\n-----------------------------------------\nSistema de cuevas Acme\n1- Crear Cueva\n2- Crear Enlace\n3- Mostrar enlaces que tiene una Cueva\n4- cambiar estado Carretera\n5- Cuevas Pozos\n6- Cambiar Direccion de enlaces\n7- Imprimir Cuevas en el Sistema\n100- salir")
    n=int(input("SELECCIONE EL NUMERO DONDE SE ENCUENTRA LA OPCION: "))
    if n==1:
        n1=input("nombre de la cueva: ")
        g.AddCave(n1)
        for key in g.Caves:
            print(key.GetName(),":",g.Caves[key])
    elif n==2:
        n1=input("Nombre del vertice origen: ")
        n2 = input("Nombre del vertice destino: ")
        n3= int(input("Ingrese la distancia entre las cuevas: "))
        origin=None
        destination=None
        for k in g.Caves:
            if k.GetName()==n1:
                origin=k
                print("Vertice de Origen:",origin.GetName())
            if k.GetName() == n2:
                destination = k
                print("Vertice de Destino:", destination.GetName())
        if origin or destination != None:
            origin.AddLinks(destination, n3,True)
    elif n==3:
        n1= input("Nombre de la cueva")
        cave = g.GetCave(n1)
        if cave:
            print("cueva busacada: ",cave.GetName())
            cave.PrintLinks()
    elif n==4:
        n1= input("Nombre de la cueva")
        cave = g.GetCave(n1)
        n2 = input("Nombre de la cueva destino donde desea cerrar la carretera con el origen")
        if cave:
            cave2=cave.GetLink(n2)
            if cave2:
                cave.ChangeLinkDirecction(cave2)
                #cave.ChangeStatusLinks(cave2)
    elif n==5:
        lista = g.Inna([])
        print("Las cuevas que son innacesibles son: ")

        for x in lista:
            print("Nombre de la cueva",x.GetName())
    elif n==6:
        n1= input("Nombre de la cueva de Origen de la carretera")
        cave = g.GetCave(n1)
        n2 = input("Nombre de la cueva destino de la carretera")
        if cave:
            cave2=cave.GetLink(n2)
            nameCave = cave2.GetName()
            if cave2:
                n=cave.ChangeLinkDirecction(cave2)
        cave2.AddLinks(n[0],n[1],n[2])
    elif n==7:
        g.PrintCaves()
    elif n==8:
        g.Grade()

        
    elif n==100:
        m=True