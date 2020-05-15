#Practica de programacion orientada a objetos

class Coche():
    """Abtraccion de los objetos coche."""
    def __init__(self,gasolina):
        self.gasolina = gasolina
        print("Tenemos " , gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No Arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan " + str(self.gasolina) + "litros")
        else:
            print("No se mueve")


#instanciando objeto, utilizando metodos y modificando atributos
mi_coche = Coche(10)
print(mi_coche.gasolina)
mi_coche.arrancar()
mi_coche.conducir()
