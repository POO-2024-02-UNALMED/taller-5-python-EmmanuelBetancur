class Zona:
    def __init__(self, nombre, zoologico=None):
        self.nombre = nombre
        self.zoologico = zoologico
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)
    
    #get y set
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getZoologico(self):
        return self.__zoologico

    def setZoologico(self, zoologico):
        self.__zoologico = zoologico

    def getAnimales(self):
        return self.__animales
