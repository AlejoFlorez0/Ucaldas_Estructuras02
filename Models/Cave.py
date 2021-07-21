import os
import json
import random
import string
from tkinter import DoubleVar

class Cave:

    def __init__(self,Tree = None):

        if Tree is not None:
            self.Tree = Tree
        
        self.__confinit()

    # Configuración inicial para el almacenamiento de peajes
    def __confinit(self):

        if not os.path.exists('File/Cave'):
            os.makedirs('File/Cave')
            
        self.cavePath = 'File//Cave//'

    # Settea la variable de nombre
    def setName(self,name):
        self.name = name
    
    # Obtiene el nombre
    def getName(self):
        return self.name

    # Settea la variable de nombre
    def setXPosition(self,xPosition):
        self.xPosition = xPosition
    
    # Obtiene el nombre
    def getXPosition(self):
        return float(self.xPosition)

    # Settea la variable de nombre
    def setYPosition(self,yPosition):
        self.yPosition = yPosition
    
    # Obtiene el nombre
    def getYPosition(self):
        return float(self.yPosition)

    # Obtendrá todos los enlaces
    def GetLinks(self):
        return self.links

    # Agregará un nuevo enlace entre cuevas
    def setLinks(self, selectedLinks):
        self.links = []
        for link in selectedLinks:
            self.links.append({"Cave":link,"state":True})
    
    # Agregará el valor de los enlaces desde json
    def setLinksFromJson(self,links):
        self.links = []
        for link in links:
            self.links.append(link)

    # Obtendrá un enlace en especifico mediante su nombre
    def GetLinkByName(self, name):
        for x in self.links:
            if name == x.GetName():
                return x
            return None

    # Guardará un archivo del json
    def save(self):

        jsonFile = {'id': self.name, 'name': self.name,'xPosition': self.xPosition,'yPosition': self.yPosition, 'links' : self.links}

        with open(self.cavePath+self.name+'.json','w') as json_file:
            json.dump(jsonFile, json_file)

        return True

    # Guardará un archivo del json
    def update(self):

        jsonFile = {'id': self.name, 'name': self.name,'xPosition': self.xPosition,'yPosition': self.yPosition}

        with open(self.cavePath+self.name+'.json','w') as json_file:
            json.dump(jsonFile, json_file)

        return True

    # Cargará un peaje desde un archivo json
    def loadFromFile(self,fileName):
        file = open (self.cavePath+fileName, "r")
        data = json.loads(file.read())

        self.setName(data['name'])
        self.setXPosition(data['xPosition'])
        self.setYPosition(data['yPosition'])
        self.setLinksFromJson(data['links'])
        
        # Closing file
        file.close()
