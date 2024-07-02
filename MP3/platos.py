##############################################################
from random import randint, choice, seed
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 1.1 ###
#Esta clase debe poseer los siguientes atributos:
#• nombre: Es un str que corresponde al nombre del plato. Este se recibe como
#parámetro de inicialización.
#• calidad: Es un int que representa la calidad del plato. Se inicializa en 0
class Plato:
    def __init__(self,nombre):
        self.nombre=nombre
        self.calidad = 0
    pass
### FIN PARTE 1.1 ###

### INICIO PARTE 1.2 ###
#Esta clase debe heredar de la clase Plato. Además, esta clase debe poseer los
#siguientes atributos adicionales:
#• tamano: Es un str que representa el tamaño del bebestible. Debe inicializarse
#eligiendo aleatoriamente entre los strings "Pequeño", "Mediano" y "Grande".
#• dificultad: Es un int que representa la dificultad del plato. Si el tamaño es
#"Pequeño" debe inicializarse en 3, si el tamaño es "Mediano" debe
#inicializarse en 6 y si el tamaño es "Grande" debe inicializarse en 9.
#• calidad: Es un int que representa la calidad del bebestible. Debe inicializarse
#en un número entero aleatorio entre 3 y 8
class Bebestible(Plato):
    tamano = ""
    dificultad = ""
    calidad = 0
    
    
    def __init__(self):
        self.tamano = self.cargarTamano()
    
    def cargarTamano(self):
        for i in range(3):
            if i == 1:
                tamano = "Pequeño"
                print("tamano: {}", format(tamano))
            if i == 2:
                tamano = "Mediano"
                print("tamano: {}", format(tamano))
            if i == 3:
                tamano = "Grande"
                print("tamano: {}", format(tamano))
            value = tamano
    
        return value       
    
    def cargarDificultad(self):
        for i in range(3):
            seed(1)
            value = randint(1,3)
            if i == 1:
                print("OPCION: {}", value)
                dificultad = 3
            if i == 2:
                print("OPCION: {}", value)
                dificultad = 6
            if i == 3:
                print("OPCION: {}", value)
                dificultad = 9
            value = dificultad
        return value   

    def cargarVariables(self):
        for i in range(3):
            seed(1)
            randomCalidad = randint(3,8)
            if i == 1:
                calidad = randomCalidad
            if i == 2:
                calidad = randomCalidad
            if i == 3:
                calidad = randomCalidad
            value = calidad
        return value 
### FIN PARTE 1.2 ###

### INICIO PARTE 1.3 ###
class Comestible:
    pass
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
