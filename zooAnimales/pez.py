from .animal import Animal


class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0


    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)
        Animal.peces += 1

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "océano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "océano", genero, "gris", 6)

    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)

    def movimiento(self):
        return "nadar"
    
    # Getters y Setters
    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self.cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self.cantidadAletas = cantidadAletas
