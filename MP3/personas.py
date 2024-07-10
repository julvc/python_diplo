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
        tiempo_entrega = 0
        factor_tamano = 0
        factor_velocidad = 0
        if tamanioPedidos >= 0 or tamanioPedidos <= 2:
            factor_tamano = 5
            factor_velocidad = 1.25
        else:
            factor_tamano = 15
            factor_velocidad = 0.85
        
        tiempo_entrega = factor_tamano * factor_velocidad
        return tiempo_entrega
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):   
    def __init__(self, nombre, habilidad):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50, 80)
        
    def cocinar(self,informacion_plato):
        preparacion = ""
        factor_calidad = 0
        if informacion_plato[1] == "Bebestible":
            preparacion = Bebestible(informacion_plato[0])
        else:
            preparacion = Comestible(informacion_plato[0])
        
        if informacion_plato[1] == "Comestible":
                self.energia -= 15
        elif informacion_plato[1] == "Bebestible":
            if preparacion.tamano == "Pequeño":
                    self.energia -= 5
            elif preparacion.tamano == "Mediano":
                    self.energia -= 8
            else:
                    self.energia -= 10
        if preparacion.calidad > self.habilidad:
            preparacion.calidad = preparacion.dificultad * 0.7
        else:
            preparacion.calidad = preparacion.dificultad * 1.5
        return preparacion
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self,nombre,platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos #ES UN DICCIONARIO Y NO UNA LISTA

    def recibir_pedido(self, pedido, demora):
        calificacion = 10
        if len(pedido) < len(self.platos_preferidos) or demora >= 20:
            calificacion = calificacion / 2
        
        for values in pedido.values():
            bebestible = Bebestible("")
            comestible = Comestible("")
            if values.__class__.__name__ == "Bebestible":
                bebestible = values
                if bebestible.calidad >= 11:
                    calificacion += 1.5
                if bebestible.calidad <= 8:
                    calificacion -= 3
                if calificacion < 0:
                    calificacion = 0
            else:
                comestible = values
                if comestible.calidad >= 11:
                    calificacion += 1.5
                if comestible.calidad <= 8:
                    calificacion -= 3
                if calificacion < 0:
                    calificacion = 0
            
        return calificacion         
### FIN PARTE 2.4 ###


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for key, plato in un_cliente.platos_preferidos.values():
            #print(f" - {plato[1]}: {plato[0]}")
            print(f" - {key}: {plato}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")