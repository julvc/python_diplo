import parametros as p
import random


# NO MODIFICAR
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion, tipo):
        if accion == "acelerar":
            if tipo == "automovil":
                self.resistencia_actual -= 5
            elif tipo == "moto":
                self.resistencia_actual -= 3
        elif accion == "frenar":
            if tipo == "automovil":
                self.resistencia_actual -= 10
            elif tipo == "moto":
                self.resistencia_actual -= 7
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"


# NO MODIFICAR
def seleccionar(vehiculos):
    if not len(vehiculos):
        print("No hay vehículos instanciados todavía")
        return

    print("Los vehículos disponibles son:")
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())

    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo


# Parte 1: Definición de clases

def avanzar(velocidad, tiempo):
    #TODO: Completar velocidad = float | tiempo =  int ambos valores deben ser enviados correctamente
    
    #Recibe como argumento un float que corresponde a la velocidad del vehículo en m/s y un int que corresponde al
    #tiempo expresado en segundos. Entrega la cantidad de kilómetros
    #avanzados en un rango de tiempo dado de acuerdo con la siguiente fórmula:
    #kilometraje = (velocidad en m/s * tiempo en segundos) / 1000
    #Esta función retorna los kilómetros avanzados durante el tiempo ingresado si
    #se viaja a la velocidad indicada.
    
    kilometraje = (velocidad * tiempo) / 1000
    return kilometraje


class Automovil:
    # Completar
    ruedasList = []
    ruedaDelanteraIzquierda = Rueda
    ruedaDelanteraDerecha = Rueda
    ruedaTraseraIzquierda = Rueda
    ruedaTraseraDerecha = Rueda
    ruedasList.append(ruedaDelanteraIzquierda)
    ruedasList.append(ruedaDelanteraDerecha)
    ruedasList.append(ruedaTraseraIzquierda)
    ruedasList.append(ruedaTraseraDerecha)
    aceleracion = 0 #Corresponde a la aceleración del vehículo medida en km/h cuadrado2. Se inicializa en 0
    velocidad = 0 #Corresponde a la velocidad del vehículo medida en km/h. Se inicializa en 0
    
    
    def __init__(self, kilometraje,ano):
        self.kilometraje = kilometraje
        self.ano = ano
        #self.ruedas = ruedasList
        #self.aceleracion = aceleracion
        #self.velocidad = velocidad

    def __str__(self):
        return f"Automóvil del año {self.ano}."
    
    def avanzar_tiempo_auto(self, tiempo):
        tiempoConvertido = tiempo/3.6
        kilometraje = avanzar(self.velocidad,tiempoConvertido)
        print("METODO AVANZAR TIEMPO AUTO. Kilometraje: " + kilometraje)
        pass

    def acelerar_tiempo_auto(self, tiempo):
        # Primero debes transformar el tiempo de segundos a horas OK
        # luego sumar tiempo en horas * 0.5 al atributo aceleración. OK
        # Luego incrementa la velocidad del vehículo según el nuevo atributo aceleración de acuerdo con la fórmula velocidad += aceleración * tiempo en horas. OK
        # Luego llama al método avanzar(tiempo), entregándole como atributo el tiempo en segundos recibido inicialmente
        # Ejecuta el método gastar() de cada uno de los objetos guardados en la lista de ruedas entregándole como argumento el string “acelerar” y el tipo “automovil". 
        # Finalmente, devuelve el atributo aceleración a 0.
        
        tiempoConvertido = tiempo/3600
        self.aceleracion+= tiempoConvertido * 0.5
        self.velocidad+= self.aceleracion * tiempoConvertido
        self.avanzar_tiempo_auto(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("acelerar", "automovil")
            
        self.aceleracion = 0
        
    def frenar_auto(self, tiempo):
    #Primero debes transformar el tiempo de segundos a horas, y restar tiempo en horas * 0.5 al atributo aceleración.  OK
    # Luego, disminuye la velocidad del vehículo de acuerdo con el nuevo atributo aceleración, 
    # con la fórmula velocidad += aceleración * tiempo en horas (dado que aceleración tendrá un valor negativo en ese momento, 
    # realizar esta suma disminuirá la velocidad). Si la velocidad queda negativa, se tiene que dejar en 0. OK

    # Después llama al método avanzar(tiempo) entregándole como atributo el tiempo en segundos recibido inicialmente 
    # Luego, ejecuta el método gastar() de cada uno de los objetos guardados en la lista de ruedas entregándole como argumento 
    # el string “frenar” y el string “automovil". OK
    #Finalmente devuelve el atributo aceleración a 0 OK
        tiempoConvertido = tiempo/3600
        self.aceleracion-= tiempoConvertido * 0.5
        self.velocidad+= self.aceleracion * tiempoConvertido
        if self.velocidad < 0:
            self.velocidad = 0
        
        self.avanzar_tiempo_auto(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("frenar", "automovil")
        
        self.aceleracion = 0
        
        
    def obtener_kilometraje():
        #return kilometraje
        pass
    
    def reemplazar_rueda():
        pass

class Moto:
    # Completar
    ruedasList = []
    ruedaDelantera = Rueda
    ruedaTrasera = Rueda
    ruedasList.append(ruedaDelantera)
    ruedasList.append(ruedaTrasera)
    
    def __init__(self, cilindrada):
        self.cilindrada = cilindrada
        pass
    
    def __str__(self):
        return f"Moto del año {self.ano}."
    
    def avanzar_moto(self, tiempo):
        self.tiempo = tiempo
        pass
    def acelerar_moto(self, tiempo):
        self.tiempo = tiempo
        pass
    def frenar_moto(self, tiempo):
        self.tiempo = tiempo
        pass
    def obtener_kilometraje():
        pass
    def reemplazar_rueda():
        pass


# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    # Completar
    if opcion == 2:  # Acelerar
        pass
    elif opcion == 3:  # Frenar
        pass
    elif opcion == 4:  # Avanzar
        pass
    elif opcion == 5:  # Cambiar rueda
        pass
    elif opcion == 6:  # Mostrar Estado
        pass


def main():
    vehiculos = []

    # Parte 3: Completar código principal
    # Completar
    # Aquí debes instanciar los dos objetos pedidos
    # y agregarlos a la lista de vehículos

    # NO MODIFICAR
    vehiculo = None

    dict_opciones = {
        1: ("Seleccionar Vehiculo", seleccionar),
        2: ("Acelerar", accion),
        3: ("Frenar", accion),
        4: ("Avanzar", accion),
        5: ("Reemplazar Rueda", accion),
        6: ("Mostrar Estado", accion),
        0: ("Salir", None)
    }

    opcion = -1
    while opcion != 0:

        for llave, valor in dict_opciones.items():
            print(f"{llave}: {valor[0]}")

        try:
            opcion = int(input("Opción: "))
            print()

        except ValueError:
            print("Ingrese opción válida.")
            opcion = -1

        if opcion != 0 and opcion in dict_opciones.keys():
            if opcion == 1:
                vehiculo = dict_opciones[opcion][1](vehiculos)
            else:
                if vehiculo is None and vehiculos:
                    vehiculo = vehiculos[0]
                if vehiculo is None:
                    print("Aún no hay vehículos...")
                else:
                    dict_opciones[opcion][1](vehiculo, opcion)
        elif opcion == 0:
            pass
        else:
            print("Ingrese opción válida.")
            opcion = -1

        print()


if __name__ == "__main__":
    main()
