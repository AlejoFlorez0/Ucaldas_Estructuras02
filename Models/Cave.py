import os
import json
import random
import string

class Cave:

    def __init__(self,Tree = None):

        if Tree is not None:
            self.Tree = Tree
        self.__confinit()

    # Settea la variable id
    def setId(self,id):
        self.id = id

    # Obtiene el id
    def getId(self):
        return self.id

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
        return self.xPosition

    # Settea la variable de nombre
    def setYPosition(self,yPosition):
        self.yPosition = yPosition
    
    # Obtiene el nombre
    def getYPosition(self):
        return self.yPosition

    # Configuración inicial para el almacenamiento de peajes
    def __confinit(self):

        if not os.path.exists('File/Cave'):
            os.makedirs('File/Cave')
        
        self.cavePath = 'File//Cave//'
        
    # Guardará un archivo del json
    def save(self):

        caveId = self.__get_random_string()
        jsonFile = {'id': caveId, 'name': self.name,'xPosition': self.xPosition,'yPosition': self.yPosition}

        with open(self.cavePath+caveId+'.json','w') as json_file:
            json.dump(jsonFile, json_file)

        return True

    # Cargará un peaje desde un archivo json
    def loadFromFile(self,fileName):
        file = open (self.cavePath+fileName, "r")
        data = json.loads(file.read())

        self.setId(data['id'])
        self.setName(data['name'])
        self.setXPosition(data['xPosition'])
        self.setYPosition(data['yPosition'])
        
        # Closing file
        file.close()

    # Obtendra un string único para almacenar el json
    def __get_random_string(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(8))
