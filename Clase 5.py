# animal
# perro (animal)
# aguila (animal)

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "Estoy comiendo"


class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return "Estoy corriendo"


class Aguila(Animal):
    def volar(self):
        return "Estoy volando"


if __name__ == "__main__":
    perro = Perro(cantidad_patas=4, tipo="vertebrado", nombre="Fido", raza="Labrador")
    print(perro.raza)  # Output: Labrador
    print(perro.nombre)  # Output: Fido

    aguila = Aguila(cantidad_patas=2, tipo="vertebrado")
    print(aguila.comer())  # Output: Estoy comiendo
    print(aguila.volar())  # Output: Estoy volando
