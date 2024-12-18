from .animal import Animal


class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0


    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)
        Animal.reptiles += 1

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)

    def movimiento(self):
        return "reptar"
    
      # Getters y Setters
    def getColorEscamas(self):
        return self.__colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas

    def getLargoCola(self):
        return self.__largoCola

    def setLargoCola(self, largoCola):
        self.__largoCola = largoCola

     # Getters y Setters
    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getLargoCola(self):
        return self.largoCola

    def setLargoCola(self, largoCola):
        self.largoCola = largoCola
