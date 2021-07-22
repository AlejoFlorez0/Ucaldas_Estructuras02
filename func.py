class Cave:

    def __init__(self, name):
        self.name = name
        self.links = {}
        self.supplies = []
        self.status = False
        self.coste = [float('inf'), None]

    def setStatus(self, status):
        self.status = status;

    def getStatus(self):
        return self.status;

    def addAdjacentVertex(self, adjacentVertex, weight):
        self.links[adjacentVertex] = weight;

    def getWeight(self, adjacentVertex):
        return self.links[adjacentVertex]

    def getCosteValue(self):
        return self.coste[0]

    def getCosteVertex(self):
        return self.coste[1]

    def setCosteInfo(self, value, vertexLabel):
        self.coste = [value, vertexLabel]

    def AddLinks(self, destination, distance, state):
        distances = []
        if destination in self.links:
            distances = self.links[destination]
        distances.append({"Distancia": distance, "Estado": state})
        self.links[destination] = distances

    def GetName(self):
        return self.name

    def GetLink(self, name):
        for x in self.links:
            if name == x.GetName():
                return x
            return x

    def GetLinks(self):
        return self.links

    def PrintLinks(self):
        for x in self.links:
            for y in self.links[x]:
                dis = y["Distancia"]
                if y["Estado"] == False:
                    st = "CERRADO"
                else:
                    st = "ABIERTO"
                print(f"Enlace hacia {x.GetName()}, DISTANCIA : {dis} Metros, Estado:", st)

    def ChangeStatusLinks(self, destination):
        m = int(input("Distancia del enlace que desea cambiar: "))
        ListLinks = self.links[destination]
        for x in ListLinks:
            if x["Distancia"] == m:
                if x["Estado"] == False:
                    x["Estado"] = True
                else:
                    x["Estado"] = False

    def ChangeLinkDirecction(self, destination):
        m = int(input("Distancia del enlace que desea cambiar: "))
        ListLinks = self.links[destination]
        newLink = []
        for x in self.links:
            for y in ListLinks:
                if y["Distancia"] == m:
                    x.name = self.GetName()
                    newLink.append(x)
                    newLink.append(y["Distancia"])
                    newLink.append(y["Estado"])
                    del self.links[x]
                    return newLink
                return newLink


"""cueva1=Cueva("manizales")
cueva2=Cueva("medellin")
cueva1.AgregarEnlace(cueva2,10)
cueva1.AgregarEnlace(cueva2,15)
for etiqueta,valor in cueva1.ObtenerEnlaces().items():
    print(f"cueva : {cueva1.ObtenerNombre()} con enlace en {etiqueta} y distancia de: {valor}")"""


class Graph:
    def __init__(self):
        self.Caves = {}

    def AddCave(self, name):
        c = Cave(name)
        entry = input("Desea colocar un id?: ")
        if "s" in entry:
            entry = input("Por favor escriba el id de la cueva: ")
            self.Caves[c] = entry
        else:
            self.Caves[c] = None
        return c

    def GetCave(self, name):
        for x in self.Caves:
            if name == x.GetName():
                return x
        return x

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

    def recorridoProfundidad(self, cueva, lista):
        for x in cueva.links:
            if x not in lista:
                lista.append(x)
                lista = self.recorridoProfundidad(x, lista)
        return lista

    def recorridoAnchura(self, cueva, lista, original):
        for x in cueva.links:
            if x not in lista:
               lista.append(x)
        for x in cueva.links:
            for y in x.links:
                lista.append(y)
        for x in cueva.links:
            for y in x.links:
                lista = self.recorridoAnchura(y, lista, original)
        return lista


    def Boruvka(self, lista):
        e = []
        for x in g.Caves:
            n = float("inf")
            a = None
            b = None
            for y in x.links:
                for z in x.links[y]:
                    if z["Distancia"] < n and z["Estado"]:

                        n = z["Distancia"]
                        a = z
                        b = y

                        e.append(b.GetName())
            if n != float("inf"):
                lista.append([x, a, b])
        return(lista)

    def sacarListasBoruvka(self, listaBoruvka):
        lista = []
        for x in listaBoruvka:
            if lista == []:
                lista.append([x[0].GetName()])
            else:
                b = True
                for y in lista:
                    if x[0].GetName() in y:
                        b = False
                if b:
                    lista.append([x[0].GetName()])
            for y in listaBoruvka:
                n = 0
                for z in lista:
                    if y != None:
                       if y[0].GetName() in lista[n] and y[2].GetName() not in lista[n]:
                          lista[n].append(y[2].GetName())
                       if y[2].GetName() in lista[n] and y[0].GetName() not in lista[n]:
                          lista[n].append(y[0].GetName())
                       n = n + 1
        return lista

    def Boruvka2(self, lista):
        listaAcum = []

        for x in g.Caves:
            n = float("inf")
            e = None
            b = None
            for y in x.links:
                for z in x.links[y]:
                    for a in lista:
                         print(f"Nombre y: {y.GetName()} Nombre x: {x.GetName()}  y {a}")
                         if (z["Distancia"] < n and z["Estado"]) and (y.GetName() not in a and x.GetName() in a):
                             print("Entró")
                             n = z["Distancia"]
                             e = z
                             b = y
            if n != float("inf"):
                listaAcum.append([x, e, b])

        p = float("inf")
        a = None
        l = None
        for x in listaAcum:
            if x[1]["Distancia"] < p:
                p = x[1]["Distancia"]
                l = x
        return(l)


    def kruskal(self, Cueva, lista, listaprimm):
        if Cueva:
            if lista == []:
               for y in Cueva.links:
                  for z in Cueva.links[y]:
                      listaprimm.append([Cueva, z, y])
                  listaprimm = self.kruskal(y, [], listaprimm)
        return listaprimm

    def listadecuevas(self, Cueva, lista, listaprimm):
        if Cueva:
            if lista == []:
               for y in Cueva.links:
                  for z in Cueva.links[y]:
                      if Cueva not in listaprimm:
                         listaprimm.append(Cueva)
                      if y not in listaprimm:
                          listaprimm.append(y)
                  listaprimm = self.listadecuevas(y, [], listaprimm)
        return listaprimm

    def kruskal2(self, listaprimm, listaaux, listaa):
        n = float('inf')
        a = None
        b = None
        p = True
        s = []
        while p:
            print("Hola 1")
            for x in listaprimm:
                print("Hola 2")
                if x[1]["Distancia"] < n and x[1]["Estado"] and x not in listaa:
                    print("Hola 3")
                    n = x[1]["Distancia"]
                    a = x[0]
                    b = x[2]
                    c = x[1]
                    if b not in s:
                        print("Hola 4")
                        s.append(b)
                    if a not in s:
                        print("Hola 5")
                        s.append(a)
            if n != float('inf'):
                 print("Hola 6")
                 listaa.append([a, c, b])
                 ##listaprimm.remove([a, c, b])
            for f in s:
                print(f.GetName())
                print("Hola 7")
                if f not in listaaux:
                    p = False
        return listaa


class Algorithms:

    def __init__(self, algorithmId, v_from, v_to, graph, link):
        self.g = graph
        self.link = link
        if (algorithmId == 1):
            return self.Dijkstra(v_from, v_to, v_from, self.g)

    #########################################
    ### Dijkstra Algorithm
    #########################################
    def Dijkstra(self, v_from, v_to, originalFrom, G):
        current_v = G.GetCave(v_from)
        # if current_v is the origin vertex, then the coste from itself is 0
        if not current_v.getCosteVertex():
            print("start vertex: ", current_v.GetName())
            current_v.setCosteInfo(0, current_v.GetName())
        print("----------------------------------------------------------------")
        print("----------- processing each connection of ", current_v.GetName(), " ------------------")
        # for each adjacent vertex from current vertice is necessary to check all values to get the minor and replace
        for v in current_v.links:
            print("Before: ", v.GetName(), " [", v.getCosteValue(), " - ", v.getCosteVertex(), "]")
            for y in current_v.links[v]:
                weightInfo = y
                self.link = weightInfo
            if (not v.getCosteVertex() or (v.getCosteValue() > (current_v.getCosteValue() + weightInfo["Distancia"]))):
                v.setCosteInfo((current_v.getCosteValue() + weightInfo["Distancia"]), current_v)
                print("Later: ", v.GetName(), " [", v.getCosteValue(), " - ", v.getCosteVertex().GetName(), "]")

        # mark the current_v as visited to discard it for future coste evaluations
        current_v.setStatus(True)
        print(f"Se cambio el status de {current_v.GetName()} a {current_v.getStatus()}")
        # Now, it's necessary to get the new curent_v with min value on the graph (no visited vertexes)
        current_v = self.getMinVertexCosteValue(current_v)

        # if exists the new vertex then process it, but else show a message with no route found
        if (current_v):
            print("-----------------------------")
            print("new current_v: ", current_v.GetName())

            if (current_v.GetName() == v_to):
                pathway = self.getPathway(current_v, originalFrom)
                print("La ruta con menor coste desde ", originalFrom, " hasta ", v_to, " es: ", pathway,
                      ", con coste de: ", current_v.getCosteValue())
            else:
                print(current_v.GetName(), v_to, originalFrom, G)
                self.Dijkstra(current_v.GetName(), v_to, originalFrom, G)
        else:
            print("Sin ruta desde ", originalFrom, " hasta ", v_to)

    # Method to get the vertex with min value of coste
    def getMinVertexCosteValue(self, current_v):
        minValue = float('inf')
        minVertex = None
        for v in self.g.Caves:
            print("--------------------- Status of ", v.GetName(), ": ", v.getStatus(), " with value: ", v.getCosteValue());
            if (v.getCosteValue() < minValue and not v.getStatus()):
                minValue = v.getCosteValue()
                minVertex = v
                print("Ahora minVertex es: ", minVertex.GetName())
        return minVertex

    # Method to process the coste value and vertex for pathway
    def getPathway(self, current_v, originalFrom, pathway=''):
        if (current_v.GetName() == originalFrom):
            return (current_v.GetName() + ' - ' + pathway)
        else:
            if (pathway == ''):
                pathway = current_v.GetName()
            else:
                pathway = current_v.GetName() + " - " + pathway
            return self.getPathway(current_v.getCosteVertex(), originalFrom, pathway)

g = Graph()

g.AddCave("A")
g.AddCave("B")
g.AddCave("C")
g.AddCave("D")
g.AddCave("E")
g.AddCave("F")
g.AddCave("G")
g.AddCave("H")
g.AddCave("I")

m = False

while m == False:
    print(
        "\n-----------------------------------------"
        "\nSistema de cuevas Acme"
        "\n1- Crear Cueva"
        "\n2- Crear Enlace"
        "\n3- Mostrar enlaces que tiene una Cueva"
        "\n4- cambiar estado Carretera"
        "\n5- Cuevas Pozos"
        "\n6- Comprobar conexiones entrantes y salientes"
        "\n7- Comprobar cuevas innacesibles"
        "\n8- Cambiar Dirección"
        "\n9- Recorrido Minimo"
        "\n10- Pozos"
        "\n100- salir")

    n = int(input("SELECCIONE EL NUMERO DONDE SE ENCUENTRA LA OPCION: "))

    if n == 1:
        n1 = input("nombre de la cueva: ")
        g.AddCave(n1)
        for key in g.Caves:
            print(type(key), key.GetName(), ":", g.Caves[key])

    elif n == 2:
        n2 = input("Nombre del vertice origen: ")
        n3 = input("Nombre del vertice destino: ")
        n4 = int(input("Ingrese la distancia entre las cuevas: "))
        origin = None
        destination = None
        for k in g.Caves:
            if k.GetName() == n2:
                origin = k
                print("Vertice de Origen:", origin.GetName())
            if k.GetName() == n3:
                destination = k
                print("Vertice de Destino:", destination.GetName())
        if origin or destination != None:
            origin.AddLinks(destination, n4, True)

    elif n == 3:
        n5 = input("Nombre de la cueva")
        cave = g.GetCave(n5)
        if cave:
            print("cueva busacada: ", cave.GetName())
            cave.PrintLinks()

    elif n == 4:
        n6 = input("Nombre de la cueva")
        cave = g.GetCave(n6)
        n7 = input("Nombre de la cueva destino donde desea cerrar la carretera con el origen")
        if cave:
            cave2 = cave.GetLink(n7)
            print(cave2.GetName())
            if cave2:
                cave.ChangeStatusLinks(cave2)

    elif n == 5:
        lista = g.pozos([])

        for x in lista:
            print(x.GetName())

    elif n == 6:
        g.Grade()

    elif n == 7:
        lista = g.Inna([])
        print("Las cuevas que son innacesibles son: ")

        for x in lista:
            print(x.GetName())

    elif n == 8:
        nn = input("Nombre de la cueva")
        cave = g.GetCave(nn)
        print(cave)
        nn1 = input("Nombre de la cueva destino donde desea cerrar la carretera con el origen")
        if cave:
            cave2 = cave.GetLink(nn1)
            if cave2:
                n = cave.ChangeLinkDirecction(cave2)
        cave2.AddLinks(n[0], n[1], n[2])
        print(cave2.links)

    elif n == 9:
        name = input("Ingrese nombre: ")
        name2 = input("Ingrese nombre 2: ")

        Algorithms(1, name, name2, g, {});

    
        

    elif n == 10:
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
        for y in lista2:
            print(y.GetName())

    elif n == 11:
        lista = []
        listab = []
        b = True

        listaBoruvka = g.Boruvka([])
        listab = (g.sacarListasBoruvka(listaBoruvka))
        a = g.Boruvka2(listab)
        if a:
           listaBoruvka.append(a)
        listab = (g.sacarListasBoruvka(listaBoruvka))

        print(listab)
        print("Lista de Boruvka: ", listaBoruvka)
        for P in listaBoruvka:
                print(P[0].GetName(), P[1], P[2].GetName())

    elif n == 12:
        cueva = input("Ingrese la cueva origen: ")

        lista = []
        lista2 = []

        for x in g.Caves:
            if x.GetName() == cueva:
                lista = g.kruskal(x, lista, lista)

        for x in g.Caves:
            if x.GetName() == cueva:
                lista2 = g.listadecuevas(x, [], [])

        for P in lista:
            print(P)

        ##for P in lista2:
            ##print(P.GetName())

        lista3 = g.kruskal2(lista, lista2, [])

        print(lista3)

    elif n == 100:
        m = True
