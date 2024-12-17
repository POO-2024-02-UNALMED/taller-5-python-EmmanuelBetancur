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


    def toString(self):
        base = f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}"
        if self.zona:
            return base + f", la zona en la que me ubico es {self.zona.nombre}, en el {self.zona.zoologico.nombre}."
        return base
    
     # Getters y Setters
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getZona(self):
        return self.zona

    def setZona(self, zona):
        self.zona = zona
