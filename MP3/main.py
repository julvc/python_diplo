##############################################################
from random import seed
from personas import Cliente,Cocinero, Repartidor
from restaurante import Restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 4 ###

#crear_repartidores(): No recibe parámetros. Crea 2 repartidores de la clase
#Repartidor (con sus parámetros correspondientes) y los agrega a una lista.
#Finalmente retorna la lista - OK
def crear_repartidores():
    repartidorUno = Repartidor("Cristiano",25)
    repartidorDos = Repartidor("Alexis", 30)
    listadoRepartidores = [repartidorUno, repartidorDos]
    return listadoRepartidores


#• crear_cocineros(): No recibe parámetros. Crea 5 cocineros de la clase
#Cocinero (con sus parámetros correspondientes) y los agrega a una lista.
#Finalmente retorna la lista. - OK
def crear_cocineros():
    cocineroUno = Cocinero("Alexa",10)
    cocineroDos = Cocinero("Monica",9)
    cocineroTres = Cocinero("Max",8)
    cocineroCuatro = Cocinero("Martin",7)
    cocineroCinco = Cocinero("Ramona",6)
    listadoCocineros = [cocineroUno,cocineroDos,cocineroTres,cocineroCuatro,cocineroCinco]
    return listadoCocineros    


#• crear_clientes(): No recibe parámetros. Crea 5 clientes de la clase Cliente
#(con sus parámetros correspondientes) y los agrega a una lista. Finalmente
#retorna la lista.
def crear_clientes():
    clienteUno = Cliente("Kobe", {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Ceviche": ["Ceviche", "Comestible"],
    "Papas fritas": ["Papas fritas", "Comestible"]
    })
    
    clienteDos = Cliente("Shaq", {
    "Sprite": ["Sprite", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Completo": ["Completo", "Comestible"],
    "Papas fritas": ["Papas fritas", "Comestible"]
    })
    clienteTres = Cliente("Alisa", {
    "Cerveza": ["Cerveza", "Bebestible"],
    "Margarita": ["Margarita", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Chorillana": ["Chorillana", "Comestible"],
    "Ensalada": ["Ensalada", "Comestible"]
    })
    clienteCuatro = Cliente("Natalia", {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Michelada": ["Michelada", "Bebestible"],
    "Salmon ahumado": ["Salmon ahumado", "Comestible"],
    "Puré de papas": ["Puré de papas", "Comestible"]
    })
    clienteCinco = Cliente("Stephen", {
    "Michelada": ["Michelada", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Hamburguesa": ["Hamburguesa", "Comestible"],
    "Papas fritas": ["Papas fritas", "Comestible"]
    })
    listadoClientes = [clienteUno,clienteDos, clienteTres, clienteCuatro, clienteCinco]
    return listadoClientes

#• crear_restaurante(): No recibe parámetros. Crea una variable cocineros, cuyo
#valor es el retorno de la función crear_cocineros(). Luego crea una variable
#repartidores, cuyo valor es el retorno de la función crear_repartidores()

#Además, crea un restaurante de la clase Restaurante (con sus parámetros
#correspondientes). Finalmente retorna la instancia del restaurante creado. (El
#nombre del restaurante lo eliges tú)
def crear_restaurante():
    dictPlatosPreferidos = {}
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    clientes = crear_clientes()
    
    for platos in range(len(clientes)):
        dictPlatosPreferidos.update(clientes[platos].platos_preferidos)
    
    restaurante = Restaurante("Pura hambre Restobar",dictPlatosPreferidos,cocineros,repartidores)
    
    return restaurante

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Cristian", "Antonio", "Francisca", "Juan", "Jorge", "Pablo", "Luis", "Sofia", "Macarena"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("DSP")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
