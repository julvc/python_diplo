##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre, tiempo_entrega):
        self.nombre = nombre
        self.tiempo_entrega = tiempo_entrega
        self.energia = randint(75, 100)
        
    #recibe una lista de platos
    def repartir(self,pedido):
        tamanioPedidos = len(pedido)
        tiempoDemora = 0
        if tamanioPedidos <= 2:
            self.energia-= 5
            tiempoDemora = self.tiempo_entrega * 1.25
        else:  
            self.energia-= 15
            tiempoDemora = self.tiempo_entrega * 0.85
        
        return tiempoDemora
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):   
    def __init__(self, nombre, habilidad):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50, 80)
        
    def cocinar(self,informacion_plato):
        plato_cocinado = 0
        for i in range(len(informacion_plato)):
            print(type(i).__name__)
            platoSplit = informacion_plato[i]
            if type(i).__name__ == "Bebestible":
                plato_cocinado = Bebestible(platoSplit[1])
                if plato_cocinado.tamano == "Pequeño":
                    self.energia -= 5
                elif plato_cocinado.tamano == "Mediano":
                    self.energia -= 8
                else:
                    self.energia -= 10
            else:
                plato_cocinado = Comestible(platoSplit[1])
                self.energia -= 15
                
        if plato_cocinado.calidad > self.habilidad:
            plato_cocinado.dificultad = plato_cocinado.dificultad * 0.7
            
        else:
            plato_cocinado.dificultad = plato_cocinado.dificultad * 1.5
        
        return plato_cocinado
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self,nombre,platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos


#recibir_pedido(pedido, demora): Recibe como argumento el pedido, que es
#una lista de objetos de la clase Bebestible o Comestible, y la demora, que es
#un int que indica cuánto se demoró la entrega de los platos. 
# Primero se debe definir una calificación que comienza en 10. 
# Si la cantidad de platos en el pedido es menor a la cantidad de platos_preferidos del cliente o 
# si la demora es mayor o igual a 20, la calificación es dividida a la mitad. 
# Luego, por cada plato, el cliente cambiará su calificación dependiendo de la calidad del plato.
#Si la calidad del plato es mayor o igual a 11, a la calificación se le suma 1.5.
#Si la calidad es menor o igual a 8, la calificación disminuye en 3, no pudiendo
#este valor descender de 0. En cualquier otro caso la calificación se mantiene.
#Finalmente se debe retornar la calificación que el cliente le ha asignado al
#restaurante   
    def recibir_pedido(self, pedido, demora):
        calificacion = 10
        if pedido < len(self.platos_preferidos) or demora >= 20:
            calificacion = 5
        
        for i in range(len(pedido)):
            plato = pedido[i]
            if plato.calidad >= 11:
                calificacion += 1.5
            if plato.calidad <= 8:
                calificacion -= 3
            if calificacion < 0:
                calificacion = 0
            
        return calificacion        
### FIN PARTE 2.4 ###


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = [
        "Jugo Natural",
        "Empanadas",
        ]
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos:
            print(plato)
            #print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
