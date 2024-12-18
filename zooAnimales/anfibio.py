from .animal import Animal


class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)
        Animal.anfibios += 1

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)

    def movimiento(self):
        return "saltar"
    
     # Getters y Setters
    def getColorPiel(self):
        return self.colorPiel

    def setColorPiel(self, colorPiel):
        self.colorPiel = colorPiel

    def isVenenoso(self):
        return self.venenoso

    def setVenenoso(self, venenoso):
        self.venenoso = venenoso
