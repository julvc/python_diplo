import csv

archivoDisponibilidad = open("disponibilidad.txt", "r", encoding="utf-8")
diccionarioDisponibilidad = {}
paciente = ""
# nombreExamenpaciente = ""
nombrePaciente = ""
pacienteAtendido = False
for linea in archivoDisponibilidad:
    key, value = linea.split(" ")
    diccionarioDisponibilidad[key.strip()] = int(value.strip())

# print(diccionarioDisponibilidad)
archivoPacientes = {}
with open("pacientes.csv", "r") as infile:
    reader = csv.reader(infile)
    for line in reader:
        archivoPacientes[line[0]] = line[1:]


#PARA IMPRIMIR SIEMPRE LAS HORAS DISPONIBLES
def imprimirHorasDisponibles(diccionarioDisponibilidad):
    print("SE INGRESA AL METODO imprimirHorasDisponibles")
    for key, value in diccionarioDisponibilidad.items():
        print(key, value)

#CALCULO DE PACIENTE Y HORAS DISPONIBLES
def calculoHorasDisponibles(paciente):
    nombreExamen = ""
    contador = 0
    print("SE INGRESA AL METODO calculoHorasDisponibles")
    pacienteTmp = obtenerDatosPaciente(paciente)
    # print(pacienteTmp)
    print(" total examenes: " + str(len(pacienteTmp)))
    for key in diccionarioDisponibilidad.keys():
        for pac in pacienteTmp:
            if key == pac:
                nombreExamen = key
                contador+=1
                #TODO: REALIZAR OPERACIONES DE RESTA SI ES MAYOR A 0 DEVOLVER MENSAJE
                # print("VALOR ENCONTRADO")
                # print("NAME FOR KEY: " + key + " VALUE: " + str(diccionarioDisponibilidad[key.strip()]))
                if diccionarioDisponibilidad.get(key) > 0:
                    
                    diccionarioDisponibilidad[key.strip()] = diccionarioDisponibilidad[key.strip()] -1
                else:
                    pacienteAtendido = False
                # print("NAME FOR KEY: " + key + " new VALUE: " + str(diccionarioDisponibilidad[key.strip()]))

            if contador == len(pacienteTmp):
                pacienteAtendido = True
                print("Paciente fue atendido: " + pacienteAtendido)
            else:
                print("No es posible atender a " + str(paciente.upper()) + "porque no existen horas disponibles para el examen " + str(nombreExamen.upper()) + ".")


#PARA BUSCAR PACIENTE Y OBTENER SUS DATOS Y SUS EXAMENES
def obtenerDatosPaciente(paciente):
    print("SE INGRESA AL METODO obtenerDatosPaciente")
    if paciente in archivoPacientes:
        # print("Nombre paciente: " + paciente + " Examenes: " + str(archivoPacientes[paciente]))
        return archivoPacientes[paciente]

#PARA BUSCAR HORAS Y SI PACIENTE SE PUEDE ATENDER
def revisarHoraPaciente(paciente):
    print("SE INGRESA AL METODO revisarHoraPaciente")
    imprimirHorasDisponibles(diccionarioDisponibilidad) 
    examenNoDisponible = ""
    print("Se ha atendido con éxito a " + str(paciente.upper()))
    print("No es posible atender a " + str(paciente.upper()) + "porque no existen horas disponibles para el examen " + str(examenNoDisponible.upper()) + ".")


    
accionIngresada = " "
while accionIngresada != "STOP":
    imprimirHorasDisponibles(diccionarioDisponibilidad)
    accion = input("Bienvenido, ingrese la instrucción a continuación: ")
    opcionIngresada = accion.split(" ")
    accionIngresada = opcionIngresada[0].upper()
    nombrePaciente = opcionIngresada[1].capitalize()
    if accionIngresada == "STOP":
        print("accion STOP")
        break
    elif accionIngresada == "AGREGAR":
        print("accion agregar")
    elif accionIngresada == "ATENDER":
        # obtenerDatosPaciente(nombrePaciente)
        calculoHorasDisponibles(nombrePaciente)
        # revisarHoraPaciente(nombrePaciente)        
        print("Accion atender")

