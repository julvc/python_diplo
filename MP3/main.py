##############################################################
from random import seed, choice, randint
from personas import Cliente,Cocinero, Repartidor
from restaurante import Restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 4 ###
def crear_repartidores():
    repartidorUno = Repartidor(choice(NOMBRES),randint(25,30))
    repartidorDos = Repartidor(choice(NOMBRES), randint(25,30))
    listadoRepartidores = [repartidorUno, repartidorDos]
    return listadoRepartidores

def crear_cocineros():
    cocineroUno = Cocinero(choice(NOMBRES),randint(1,10))
    cocineroDos = Cocinero(choice(NOMBRES),randint(1,10))
    cocineroTres = Cocinero(choice(NOMBRES),randint(1,10))
    cocineroCuatro = Cocinero(choice(NOMBRES),randint(1,10))
    cocineroCinco = Cocinero(choice(NOMBRES),randint(1,10))
    listadoCocineros = [cocineroUno,cocineroDos,cocineroTres,cocineroCuatro,cocineroCinco]
    return listadoCocineros    

def crear_clientes():
    clienteUno = Cliente(choice(NOMBRES), choice(list(INFO_PLATOS.items())))
    clienteDos = Cliente(choice(NOMBRES), choice(list(INFO_PLATOS.items())))
    clienteTres = Cliente(choice(NOMBRES), choice(list(INFO_PLATOS.items())))
    clienteCuatro= Cliente(choice(NOMBRES), choice(list(INFO_PLATOS.items())))
    clienteCinco = Cliente(choice(NOMBRES), choice(list(INFO_PLATOS.items())))

    listadoClientes = [clienteUno,clienteDos, clienteTres, clienteCuatro, clienteCinco]
    return listadoClientes

def crear_restaurante():
    #dictPlatosPreferidos = {}
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    clientes = crear_clientes()
    
    #for platos in range(len(clientes)):
    #    dictPlatosPreferidos.update(clientes[platos].platos_preferidos)
    
    restaurante = Restaurante("Pura hambre Restobar",INFO_PLATOS,cocineros,repartidores)
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
