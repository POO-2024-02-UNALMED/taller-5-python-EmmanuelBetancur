class Zona:
    def __init__(self, nombre, zoologico):
        self.nombre = nombre
        self.zoologico = zoologico
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)
