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
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoologico(self):
        return self.zoologico

    def setZoologico(self, zoologico):
        self.zoologico = zoologico

    def getAnimales(self):
        return self.animales
