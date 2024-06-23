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
    kilometraje = (velocidad * tiempo) / 1000
    return kilometraje


class Automovil:
    # Completar
    ruedasList = []
    ruedaDelanteraIzquierda = Rueda()
    ruedaDelanteraDerecha = Rueda()
    ruedaTraseraIzquierda = Rueda()
    ruedaTraseraDerecha = Rueda()
    ruedasList.append(ruedaDelanteraIzquierda)
    ruedasList.append(ruedaDelanteraDerecha)
    ruedasList.append(ruedaTraseraIzquierda)
    ruedasList.append(ruedaTraseraDerecha)
    aceleracion = 0 #Corresponde a la aceleración del vehículo medida en km/h cuadrado2. Se inicializa en 0
    velocidad = 0 #Corresponde a la velocidad del vehículo medida en km/h. Se inicializa en 0
    
    
    def __init__(self, kilometraje,ano):
        self.kilometraje = kilometraje
        self.ano = ano


    def __str__(self):
        return f"Automóvil del año {self.ano}."
    
    def avanzar_tiempo_auto(self, tiempo):
#Recibe como argumento un int que corresponde al tiempo
#expresado en segundos. Incrementa el atributo kilometraje de acuerdo con
#el resultado de la función avanzar definida previamente.
#Recuerda que la velocidad almacenada en elatributo velocidad de la clase está medida en km/h y la función avanzar
#necesita la velocidad en m/s, por lo que deberás primero convertirla antes de
#entregar la velocidad a la función avanzar. Para convertir un valor de km/h a
#m/s, debes dividirlo por 3.6 
        velocidadConvertida = tiempo/3.6
        avanzar(self.velocidad,velocidadConvertida)

    def acelerar_tiempo_auto(self, tiempo):
        self.aceleracion+=(tiempo * 0.5)
        self.velocidad+=(self.aceleracion * tiempo)
        self.avanzar_tiempo_auto(tiempo)
        for index, rueda in enumerate(self.ruedasList):
            #print("ANTES RUEDA: " + str(index) + " resistencia_actual: " + str(rueda.resistencia_actual) + " resistencia_total: " 
            #    + str(rueda.resistencia_total) + " estado: " + str(rueda.estado))
            rueda.gastar("acelerar", "automovil")
            #print("DESPUES RUEDA: " + str(index) + " resistencia_actual: " + str(rueda.resistencia_actual) + " resistencia_total: " 
            #    + str(rueda.resistencia_total) + " estado: " + str(rueda.estado))
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
        
        
    def obtener_kilometraje(self):
        return self.kilometraje
    
    def reemplazar_rueda(self):
        contador = 0
        for rueda in range(len(self.ruedasList)):
            if self.ruedasList[rueda] == "Rota":
                self.ruedasList.pop(rueda)
                self.ruedasList.insert(rueda,Rueda)
                contador+=1
                if contador >= 2:
                    break

class Moto:
    # Completar
    ruedasList = []
    ruedaDelantera = Rueda
    ruedaTrasera = Rueda
    ruedasList.append(ruedaDelantera)
    ruedasList.append(ruedaTrasera)
    aceleracion = 0 #Corresponde a la aceleración del vehículo medida en km/h cuadrado2. Se inicializa en 0
    velocidad = 0 #Corresponde a la velocidad del vehículo medida en km/h. Se inicializa en 0
    
    def __init__(self, kilometraje,ano,cilindrada):
        self.kilometraje = kilometraje
        self.ano = ano
        self.cilindrada = cilindrada
        
    
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
    vehiculoNombre = type(vehiculo).__name__
    newVehiculo = vehiculo
    
    # Completar
    if opcion == 2:  # Acelerar
        tiempo = round(float(input("Agregue aceleración: ")))
        tiempoAceleracion = round(tiempo/3600)
        if vehiculoNombre == "Automovil":
            newVehiculo.acelerar_tiempo_auto(tiempoAceleracion)
        elif vehiculoNombre == "Moto":
            print("OPCION ACELERAR MOTO")
            #newVehiculo.acelerar_tiempo_auto(tiempoAceleracion)
        
        print("Se ha acelerado por {} segundos, llegando a una velocidad de {} km/h".format(tiempo,round(newVehiculo.velocidad,2)))
    elif opcion == 3:  # Frenar
        pass
    elif opcion == 4:  # Avanzar
        pass
    elif opcion == 5:  # Cambiar rueda
        pass
    elif opcion == 6:  # Mostrar Estado
        print("Vehiculo: {}. Año: {}, Velocidad: {}km/h, Kilometraje: {}".format(vehiculoNombre,newVehiculo.ano,round(newVehiculo.velocidad,2),newVehiculo.kilometraje))
        print("Rueda delantera izquierda: {} \n".format(newVehiculo.ruedasList[0].estado)
            +"Rueda delantera derecha: {} \n".format(newVehiculo.ruedasList[1].estado)
            +"Rueda trasera izquierda: {} \n".format(newVehiculo.ruedasList[2].estado)
            +"Rueda trasera derecha: {}".format(newVehiculo.ruedasList[3].estado))
        
        


def main():
    vehiculos = []

    # Parte 3: Completar código principal
    # Completar
    # Aquí debes instanciar los dos objetos pedidos
    # y agregarlos a la lista de vehículos
    automovil = Automovil(10000,2024)
    moto = Moto(0,2024,0)
    vehiculos.append(automovil)
    vehiculos.append(moto)

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
