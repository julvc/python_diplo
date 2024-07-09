##############################################################
from personas import Cliente,Cocinero, Repartidor
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.califacion = 0

    def recibir_pedidos(self,clientes):
        client = Cliente()
        chef = Cocinero()
        repartidor = Repartidor()
        puedeCocinar = False
        listPlatosPreferidosClientes = {}
        pedidos = {} # PLATOS COCINADOS
        calificacionRestaurante = self.calificacion  # CALIFICACION RESTAURANTE
        for i in range(len(clientes)):
            client = clientes[i]
            listPlatosPreferidosClientes.append(client.self.platos_preferidos)

        for c in range(self.cocineros):
            chef = self.cocineros[c]
            print("largo listado: " , len(self.cocineros))
            #if c == len(self.cocineros - 1):
            #    if chef.self.energia < 0:
            #        print("NO EXISTEN COCINEROS CON ENERGIA")
            if chef.self.energia > 0:
                print("cocinero: " + chef.nombre + " energia: " + str(chef.self.energia))
                puedeCocinar = True #VALIDAR QUE NO SE PUEDE COCINAR UN PLATO
                break
            if puedeCocinar:
                for j in range(len(listPlatosPreferidosClientes)):
                    #revisar el contador, de lo contrario agregar uno
                    pedidos.append(chef.self.cocinar(listPlatosPreferidosClientes[j]))
                    if chef.self.energia < 0:
                        break

        for p in range(len(pedidos)):
            #for r in range(len(repartidores)):
            #RECORRER REPARTIDORES VERIFICAR SI ES LISTA O DICCIONARIO
            if repartidor.energia > 0:
                tiempoDemora = repartidor(pedidos[p])
                #ENTREGA DE PEDIDO
                calificacion = client.recibir_pedido(pedidos[p],tiempoDemora)
                calificacionRestaurante += calificacion
            else:
                print("recibir_pedido(pedido, demora), un pedido vacío (lista vacía) y una demora igual a 0.")
                client.recibir_pedido([],0)

        self.califacion = calificacionRestaurante / len(clientes)
        pass

#2. Luego, cada plato se cocina haciendo uso de algún cocinero y su
#método cocinar(plato) para prepararlo y se agrega a una lista llamada
#pedido (sólo se puede utilizar un cocinero con energía positiva paracocinar. 
# Si no quedan cocineros que cumplan esta condición no se
#cocina el plato). TODO: OK - PERO REVISAR ENERGIA DE COCINERO

#3. Una vez que los platos se han cocinado, se calcula cuánto será la
#demora del tiempo del pedido (la lista con todos los platos cocinados)
#con algún repartidor y su método repartir(pedido) (sólo se puede
#utilizar un repartidor con energía positiva para repartir. Si no quedan
#repartidores que cumplan esta condición, se le entrega al cliente en
#recibir_pedido(pedido, demora), un pedido vacío (lista vacía) y una
#demora igual a 0.) TODO: OK - PERO REVISAR COMO RECIBO LISTADO O DICCIONARIO DE REPARTIDORES Y COMO RECORRER, VALIDAR ENERGIA REPARTIDOR

#4. Se entrega el pedido y la demora al cliente con su método
#recibir_pedido(pedido, demora).

#5. Se actualiza la calificación del restaurante sumándole la calificación
#que el cliente retorna en el paso anterior.

#6. Una vez se hayan terminado de entregar todos los pedidos, se divide
#la calificación final por la cantidad de clientes atendidos (largo de la
#lista clientes). TODO: OK - REVISAR CALIFICACION

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
