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
    aceleracion = 0
    velocidad = 0
    
    def __init__(self, kilometraje,ano):
        self.kilometraje = kilometraje
        self.ano = ano


    def __str__(self):
        return f"Automóvil del año {self.ano}."
    
    def avanzar_auto(self, tiempo):
        velocidadConvertida = float(tiempo/3.6)
        kilometraje = avanzar(self.velocidad,velocidadConvertida)
        self.kilometraje+=kilometraje

    def acelerar_auto(self, tiempo):
        tiempoEnHoras = tiempo/3600        
        self.aceleracion+=(tiempoEnHoras * 0.5)
        self.velocidad+=(self.aceleracion * tiempoEnHoras)
        self.avanzar_auto(tiempo)
        
        for rueda in self.ruedasList:
            rueda.gastar("acelerar", "automovil")

        self.aceleracion = 0
        
    def frenar_auto(self, tiempo):
        tiempoEnHoras = tiempo/3600     
        self.aceleracion-=(tiempoEnHoras * 0.5)
        self.velocidad+=(self.aceleracion * tiempoEnHoras)
        if self.velocidad < 0:
            self.velocidad = 0

        self.avanzar_auto(tiempo)
        for rueda in self.ruedasList:
            rueda.gastar("frenar", "automovil")

        self.aceleracion = 0
        
    def obtener_kilometraje(self):
        return self.kilometraje
    
    def reemplazar_rueda_auto(self):
        contadorGastada = 0
        contadorRota = 0
        for rueda in range(len(self.ruedasList)):
            if self.ruedasList[rueda].estado == "Rota":
                self.ruedasList.pop(rueda)
                self.ruedasList.insert(rueda,Rueda())
                contadorRota+=1
                if contadorRota >= 1:
                    break
            elif self.ruedasList[rueda].estado == "Gastada":
                self.ruedasList.pop(rueda)
                self.ruedasList.insert(rueda,Rueda())
                contadorGastada+=1
                if contadorGastada >= 1:
                    break
            
        if contadorRota >=1 or contadorGastada >=1:
            print("Se han reemplazado las ruedas con éxito")
        
class Moto:
    # Completar
    ruedasList = []
    ruedaDelantera = Rueda()
    ruedaTrasera = Rueda()
    ruedasList.append(ruedaDelantera)
    ruedasList.append(ruedaTrasera)
    aceleracion = 0
    velocidad = 0
    
    def __init__(self, kilometraje,ano,cilindrada):
        self.kilometraje = kilometraje
        self.ano = ano
        self.cilindrada = cilindrada #es número int no negativo
    
    def __str__(self):
        return f"Moto del año {self.ano}."
    
    def avanzar_moto(self, tiempo):
        velocidadConvertida = float(tiempo/3.6)
        kilometraje = avanzar(self.velocidad,velocidadConvertida)
        self.kilometraje+=kilometraje
    
    def acelerar_moto(self, tiempo):
        tiempoEnHoras = tiempo/3600      
        self.aceleracion+=(tiempoEnHoras * 0.8+ self.cilindrada * 0.2)
        self.velocidad+=(self.aceleracion * tiempoEnHoras * 3)
        self.avanzar_moto(tiempo)
        
        for rueda in self.ruedasList:
            rueda.gastar("acelerar", "moto")
        self.aceleracion = 0
        
    def frenar_moto(self, tiempo):
        print("tiempo: ", tiempo)
        print("OBJETO: " , self)
        tiempoEnHoras = tiempo/3600   
        self.aceleracion-=(tiempoEnHoras * 0.8+self.cilindrada * 0.2)
        print("self.aceleracion: " , self.aceleracion)
        print("self.aceleracion: {}, tiempoEnHoras: {}".format(self.aceleracion, tiempoEnHoras))
        
        self.velocidad+=(self.aceleracion * tiempoEnHoras * 2)
        print("self.velocidad: " , self.velocidad)
        
        if self.velocidad < 0:
            self.velocidad = 0

        self.avanzar_moto(tiempo)
        
        for rueda in self.ruedasList:
            rueda.gastar("frenar", "moto")

        self.aceleracion = 0
        
    def obtener_kilometraje(self):
        return self.kilometraje
    
    def reemplazar_rueda_moto(self):
        contadorGastada = 0
        contadorRota = 0
        for rueda in range(len(self.ruedasList)):
            if self.ruedasList[rueda].estado == "Rota":
                self.ruedasList.pop(rueda)
                self.ruedasList.insert(rueda,Rueda())
                contadorRota+=1
                if contadorRota >= 1:
                    break
            elif self.ruedasList[rueda].estado == "Gastada":
                self.ruedasList.pop(rueda)
                self.ruedasList.insert(rueda,Rueda())
                contadorGastada+=1
                if contadorGastada >= 1:
                    break
            
        if contadorRota >=1 or contadorGastada >=1:
            print("Se han reemplazado las ruedas con éxito")


# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    vehiculoNombre = type(vehiculo).__name__
    newVehiculo = vehiculo
    
    # Completar
    if opcion == 2:  # Acelerar
        tiempo = round(float(input("Agregue aceleración: ")))
        if vehiculoNombre == "Automovil":
            newVehiculo.acelerar_auto(tiempo)
        elif vehiculoNombre == "Moto":
            newVehiculo.acelerar_moto(tiempo)
        
        print("Se ha acelerado por {} segundos, llegando a una velocidad de {} KM/H".format(tiempo,round(newVehiculo.velocidad,2)))
    elif opcion == 3:  # Frenar
        tiempo = round(float(input("Agregue tiempo de frenado: ")))
        if vehiculoNombre == "Automovil":
            newVehiculo.frenar_auto(tiempo)
        elif vehiculoNombre == "Moto":
            newVehiculo.frenar_moto(tiempo)

        
        print("Se ha frenado por {} segundos, llegando a una velocidad de {} KM/H".format(tiempo,round(newVehiculo.velocidad,2)))
    elif opcion == 4:  # Avanzar
        tiempo = round(float(input("Agregue tiempo de desplazamiento: ")))
        if vehiculoNombre == "Automovil":
            newVehiculo.avanzar_auto(tiempo)
        elif vehiculoNombre == "Moto":
            newVehiculo.avanzar_moto(tiempo)
            
        print("Se ha avanzado por {} segundos a una velocidad de {} KM/H".format(tiempo,round(newVehiculo.velocidad,2)))

    elif opcion == 5:  # Cambiar rueda
        if vehiculoNombre == "Automovil":
            newVehiculo.reemplazar_rueda_auto()
        elif vehiculoNombre == "Moto":
            newVehiculo.reemplazar_rueda_moto()

    elif opcion == 6:  # Mostrar Estado
        kilometraje = 0
        if newVehiculo.kilometraje % 1 == 0:
            kilometraje = int(newVehiculo.kilometraje)
        else:
            kilometraje = round(newVehiculo.kilometraje,2)
        if vehiculoNombre == "Automovil":
            print("Vehiculo: {}. Año: {}, Velocidad: {} KM/H, Kilometraje: {} KM".format(vehiculoNombre,newVehiculo.ano,round(newVehiculo.velocidad,2),kilometraje))
            print("Rueda delantera izquierda: {} \n".format(newVehiculo.ruedasList[0].estado)
                +"Rueda delantera derecha: {} \n".format(newVehiculo.ruedasList[1].estado)
                +"Rueda trasera izquierda: {} \n".format(newVehiculo.ruedasList[2].estado)
                +"Rueda trasera derecha: {}".format(newVehiculo.ruedasList[3].estado))
        elif vehiculoNombre == "Moto":
            print("Vehiculo: {}. Año: {}, Velocidad: {} KM/H, Kilometraje: {} KM, Cilindrada: {}".format(vehiculoNombre,newVehiculo.ano,round(newVehiculo.velocidad,2),kilometraje, newVehiculo.cilindrada))
            print("Rueda delantera: {} \n".format(newVehiculo.ruedasList[0].estado) +"Rueda trasera: {} \n".format(newVehiculo.ruedasList[1].estado))    

def main():
    vehiculos = []

    # Parte 3: Completar código principal
    # Completar
    # Aquí debes instanciar los dos objetos pedidos
    # y agregarlos a la lista de vehículos
    automovil = Automovil(10000,2024)
    moto = Moto(1000,2024,5)
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
