class Cave:
    
    def __init__(self, name):
        self.name = name
        self.links = {}
        self.supplies =[]
        self.costeDijsktra=[float('inf'), None, False]

    def AddLinks(self, destination, distance,state):
        distances=[]
        if destination in self.links:
            distances=self.links[destination]
        distances.append({"Distancia":distance,"Estado":state})
        self.links[destination]=distances

    def GetCosteValue(self):
        return self.costeDijsktra[0]

    def GetCosteCave(self):
        return self.costeDijsktra[1]

    def GetCosteStatus(self):
        return self.costeDijsktra[2]

    def SetCosteDijsktra(self,value,cave,state):
        self.costeDijsktra=[value,cave,state]

    def GetName(self):
        return self.name

    def GetLink(self, name):
        for x in self.links:
            if name == x.GetName():
                print(x.GetName())
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

    def GetStatus(self,destination):
        if len(self.links[destination])==1:
            for x in self.links[destination]:
                return x["Estado"]
        m = int(input("Distancia del Enlace: "))
        ListLinks = self.links[destination]
        for x in ListLinks:
            if x["Distancia"] == m:
                return x["Estado"]

    def GetWeight(self,destination):
        if len(self.links[destination])==1:
            for x in self.links[destination]:
                return x["Distancia"]
        m = int(input("Distancia del Enlace: "))
        ListLinks = self.links[destination]
        for x in ListLinks:
            if x["Distancia"] == m:
                return x["Distancia"]

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


class Graph:
    def __init__(self):
        self.Caves = {}

    def pozos(self, lista):
        for x in self.Caves:
            b = True
            name = x.GetName()
            if x.links == {}:
                for y in self.Caves:
                    for z in y.links:
                        for a in y.links[z]:
                            if z.GetName() == name and a["Estado"]:
                                b = False
                if b == True:
                    lista.append(x)
        return lista

    def recorrido(self, cueva, lista):
        for x in cueva.links:
            if x not in lista:
                lista.append(x)
                lista = self.recorrido(x, lista)
        return lista

    def AddCave(self, name):
        c=Cave(name)
        entry=input("Desea colocar un id?: ")
        if "s" in entry:
            entry=input("Por favor escriba el id de la cueva: ")
            self.Caves[c]=entry
        else:
            self.Caves[c]=None
        return c

    def GetCaves(self):
        return self.Caves

    def exists(self, name):
        return name in self.Caves;

    def GetCave(self, name):
        for x in self.Caves:
            if name == x.GetName():
                return x
        return None

    def PrintCaves(self):
        for x in self.Caves:
            print(f"Nombre de la cueva: {x.GetName()}, Id: {self.Caves[x]}, Enlaces de la cueva: {x.links}, {x}")
            for y in x.links:
                print()

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

    def Inna(self, lista):
        for x in self.Caves:
            b = True
            name = x.GetName()
            for y in self.Caves:
                for z in y.links:
                    for a in y.links[z]:
                        if z.GetName() == name and a["Estado"]:
                           b = False
            if b == True:
                lista.append(x)
        return lista

    def Dijkstra(self, c_from,c_to,caveOriginal):
        current_C=self.GetCave(c_from.GetName())
        if not current_C.GetCosteCave():
            print(f"Start cave: {current_C.GetName()}")
            current_C.SetCosteDijsktra(0,current_C,True)
        print("----------------------------------------------------------------")
        print("----------- processing each connection of ", current_C.GetName(), " ------------------")
        for x in current_C.links:
            print("Before: ", x.GetName(), " [Coste:", x.GetCosteValue(), " - Viene de:", x.GetCosteCave(),"]");
            weightInfo = current_C.GetWeight(x);
            if (not x.GetCosteCave()or (x.GetCosteValue() > (current_C.GetCosteValue() + weightInfo))) and current_C.GetStatus(x) :
                x.SetCosteDijsktra((current_C.GetCosteValue() + weightInfo), current_C,False);
                print("Later: ", x.GetName(), " [Coste:", x.GetCosteValue(), " - Viene de:", x.GetCosteCave().GetName(), "]");
            if not current_C.GetStatus(x):
                current_C=None
            else:
                current_C.costeDijsktra[2]=True
                current_C = self.GetMinCaveCosteValue()
        if (current_C):
            print("-----------------------------");
            print("new current_C: ", current_C.GetName())
            if (current_C.GetName() == c_to.GetName()):
                pathway = self.PrintRoute(current_C, caveOriginal);
                print("La ruta con menor coste desde la cueva:", caveOriginal.GetName(), " hasta la cueva:", c_to.GetName(), " es: ", pathway,
                      ", con coste de: ", current_C.GetCosteValue());
            else:
                self.Dijkstra(current_C, c_to, caveOriginal)
        else:
            print("Sin ruta desde la cueva", caveOriginal.GetName(), " hasta la cueva:", c_to.GetName());

    def GetMinCaveCosteValue(self):
        minValue = float('inf');
        minCave = None;
        for x in self.Caves:
            #print("--------------------- Status of ",x, x.GetName(), ": ", x.GetCosteStatus(), " with value: ", x.GetCosteValue())
            if (x.GetCosteValue() < minValue and not x.GetCosteStatus()):
                minValue = x.GetCosteValue();
                minCave = x;
        return minCave;

    def PrintRoute(self, current_C, originalFrom, pathway=''):
        if (current_C.GetName() == originalFrom.GetName()):
            return (current_C.GetName() + ' - ' + pathway);
        else:
            if (pathway == ''):
                pathway = current_C.GetName();
            else:
                pathway = current_C.GetName() + " - " + pathway;
            return self.PrintRoute(current_C.GetCosteCave(), originalFrom, pathway);


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
                cave.ChangeStatusLinks(cave2)
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
    elif n==9:
        n1= input("Nombre de la cueva de Origen de la carretera")
        cave = g.GetCave(n1)
        n2 = input("Nombre de la cueva destino de la carretera")
        if cave:
            cave2=cave.GetLink(n2)
            if cave2:
                n=cave.GetStatus(cave2)
                print(n)
    elif n==10:
        n1 = input("Nombre de la cueva de Origen de la carretera")
        cave = g.GetCave(n1)
        n2 = input("Nombre de la cueva destino de la carretera")
        if cave:
            cave2 = g.GetCave(n2)
            print(cave2)
            if cave2:
                print("hello")
                g.Dijkstra(cave,cave2,cave)

    elif n == 11:
        lista = g.pozos([])
        for x in lista:
            print(x.GetName())

    elif n == 11:
        name = input("Ingrese nombre de la cueva: ")

        lista = []
        lista2 = []
        for x in g.Caves:
            if x.GetName() == name:
                lista.append(x)
                lista2.append(x)
                lista = g.recorridoProfundidad(x, lista)
                lista2 = g.recorridoAnchura(x, lista2, x)

        print("Recorrido en profundidad:  \n")
        for y in lista:
            print(y.GetName())

        print("Recorrido en anchura:  \n")
        

        
    elif n==100:
        m=True



