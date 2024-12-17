class Zona:
    def __init__(self, nombre, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)
    
    #get y set
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoo(self):
        return self.zoologico

    def setZoo(self, zoologico):
        self.zoologico = zoologico

    def getAnimales(self):
        return self.animales
