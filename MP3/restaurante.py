##############################################################
from personas import Cliente,Cocinero, Repartidor
from platos import Bebestible, Comestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def recibir_pedidos(self,clientes):
        client = Cliente("",{})
        chef = Cocinero(self.nombre,0)
        repartidor = Repartidor("",0)
        puedeCocinar = False
        listPlatosPreferidosClientes = {}
        pedidos = {}
        calificacionRestaurante = self.calificacion  # CALIFICACION RESTAURANTE
        for i in range(len(clientes)):
            client = clientes[i]
            listPlatosPreferidosClientes.update(client.platos_preferidos)

        for c in range(len(self.cocineros)):
            chef = self.cocineros[c]
            if chef.energia > 0:
                puedeCocinar = True #VALIDAR QUE NO SE PUEDE COCINAR UN PLATO
            if puedeCocinar:
                for key,values in listPlatosPreferidosClientes.items():
                    if values[1] == "Bebestible":
                        pedidoRealizado = Bebestible(values[0])
                    else:
                        pedidoRealizado = Comestible(values[0])
                        
                    pedidoRealizado = chef.cocinar(values)
                    pedidos.update({key: pedidoRealizado})
                    if chef.energia < 0:
                        break
        
        for r in range(len(self.repartidores)):
            repartidor = self.repartidores[r]
            if repartidor.energia > 0:
                tiempoDemora = repartidor.repartir(pedidos.values())
                calificacion = client.recibir_pedido(pedidos,tiempoDemora)
                calificacionRestaurante += calificacion
            else:
                client.recibir_pedido([],0)
        self.calificacion = calificacionRestaurante / len(clientes)
        


### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
