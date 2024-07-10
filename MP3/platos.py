##############################################################
from random import randint, choice, seed
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 1.1 ###
class Plato:
    def __init__(self,nombre):
        self.nombre=nombre
        self.calidad = 0
### FIN PARTE 1.1 ###

### INICIO PARTE 1.2 ###
class Bebestible(Plato):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.tamano = self.cargarTamano()
        self.dificultad = self.cargarDificultad(self.tamano)
        self.calidad = randint(3,8)
    
    def cargarTamano(self):
        i = randint(1,3)
        if i == 1:
            self.tamano = "Pequeño"
        if i == 2:
            self.tamano = "Mediano"
        if i == 3:
            self.tamano = "Grande"
        return self.tamano       
    
    def cargarDificultad(self, tamano):
        if tamano == "Pequeño":
            dificultad = 3
        if tamano == "Mediano":
            dificultad = 6
        if tamano == "Grande":
            dificultad = 9
        return dificultad   

### FIN PARTE 1.2 ###

### INICIO PARTE 1.3 ###
#Esta clase debe heredar de la clase Plato. Además, esta clase debe poseer los
#siguientes atributos adicionales:
#• dificultad: Es un int que representa la dificultad del plato. Debe inicializarse
#en un número entero aleatorio entre 1 y 10
#• calidad: Es un int que representa la calidad de un comestible. Debe
#inicializarse en un número entero aleatorio entre 5 y 10.
#Si ejecutas directamente el archivo platos.py, podrás probar si hay errores al
#momento de definir las clases anteriores.
class Comestible(Plato):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.dificultad = randint(1,10)
        self.calidad = randint(5,10)

### FIN PARTE 1.3 ###


if __name__ == "__main__":
    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        un_bebestible = Bebestible("Coca-Cola")
        un_comestible = Comestible("Sopa")
        print(f"Esto es una {un_bebestible.nombre} de tamaño {un_bebestible.tamano} y calidad {un_bebestible.calidad}.")
        print(f"Esto es una {un_comestible.nombre} de dificultad {un_comestible.dificultad} y calidad {un_comestible.calidad}.")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
