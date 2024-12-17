class Animal:
    totalAnimales = 0
    anfibios = 0
    aves = 0 
    mamiferos = 0
    peces = 0
    reptiles = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos : {Animal.mamiferos}\n"
                f"Aves : {Animal.aves}\n"
                f"Reptiles : {Animal.reptiles}\n"
                f"Peces : {Animal.peces}\n"
                f"Anfibios : {Animal.anfibios}")


    def __str__(self):
        base = f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}"
        if self.zona:
            return base + f", la zona en la que me ubico es {self.zona.nombre}, en el {self.zona.zoologico.nombre}."
        return base
    
     # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getHabitat(self):
        return self.__habitat

    def setHabitat(self, habitat):
        self.__habitat = habitat

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getZona(self):
        return self.__zona

    def setZona(self, zona):
        self.__zona = zona
