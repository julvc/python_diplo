import csv

archivoDisponibilidad = open("disponibilidad.txt", "r", encoding="utf-8")
diccionarioDisponibilidad = {}
paciente = ""
# nombreExamenpaciente = ""
nombrePaciente = ""
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
    # print("SE INGRESA AL METODO imprimirHorasDisponibles")
    for key, value in diccionarioDisponibilidad.items():
        print(str(key).upper()+": " +str(value))

#CALCULO DE PACIENTE Y HORAS DISPONIBLES
def calculoHorasDisponibles(paciente):
    # nombreExamen = ""
    nombreExamenFaltante = ""
    contador = 0
    pacienteTmp = obtenerDatosPaciente(paciente)
    pacienteAtendido = True
    # diccionarioDisponibilidadTmp = []
    # print(" total examenes: " + str(len(pacienteTmp)))
    # print(" total examenes valores: " + str(pacienteTmp))
    
    #RECORRER PARA VALIDAR QUE ESTAN TODOS LOS EXAMENES DISPONIBLES
    for key in diccionarioDisponibilidad.keys():
        for pac in pacienteTmp:
            if key == pac:
                if diccionarioDisponibilidad.get(key) > 0:
                    contador+=1
                else:
                    pacienteAtendido = False
                    nombreExamenFaltante = key
    
    # print("VALOR CONTADOR: " + str(contador))
    # print("LARGO EXAMENES: " + str(len(pacienteTmp)))
    
    if contador == len(pacienteTmp):
        # print("NO SE PODRA EJECUTAR NINGUNA OPERACION. CONTADOR: " +str(contador) + " LARGO EXAMENES: " + str(len(pacienteTmp)))
        for key in diccionarioDisponibilidad.keys():
            for pac in pacienteTmp:
                if key == pac:
                    # nombreExamen = key
                    if diccionarioDisponibilidad.get(key) > 0:                    
                        diccionarioDisponibilidad[key.strip()] = diccionarioDisponibilidad[key.strip()] -1
                    else:
                        pacienteAtendido = False
        # if diccionarioDisponibilidad.get(key) > 0:                    
        #     diccionarioDisponibilidad[key.strip()] = diccionarioDisponibilidad[key.strip()] -1
        # print("Se ha atendido con éxito a " + paciente.upper() +"!")
    # else:
        # print("No es posible atender a " + str(paciente.upper()) + " porque no existen horas disponibles para el examen " + str(nombreExamen.upper()) + ".")
    # for key in diccionarioDisponibilidad.keys():
    #     for pac in pacienteTmp:
    #         if key == pac:
    #             nombreExamen = key
    #             contador+=1
    #             #TODO: REALIZAR OPERACIONES DE RESTA SI ES MAYOR A 0 DEVOLVER MENSAJE
    #             # print("VALOR ENCONTRADO")
    #             # print("NAME FOR KEY: " + key + " VALUE: " + str(diccionarioDisponibilidad[key.strip()]))
    #             if diccionarioDisponibilidad.get(key) > 0:                    
    #                 diccionarioDisponibilidad[key.strip()] = diccionarioDisponibilidad[key.strip()] -1
    #             else:
    #                 pacienteAtendido = False
                # print("NAME FOR KEY: " + key + " new VALUE: " + str(diccionarioDisponibilidad[key.strip()]))
    else:
        print("No es posible atender a " + str(paciente.upper()) + " porque no existen horas disponibles para el examen " + str(nombreExamenFaltante.upper()) + ".")
    # if pacienteAtendido == True & contador == len(pacienteTmp):
    if pacienteAtendido == True:
        # pacienteAtendido = True        
        print("Se ha atendido con éxito a " + paciente.upper() +"!")
    # else:
    #     print("No es posible atender a " + str(paciente.upper()) + " porque no existen horas disponibles para el examen " + str(nombreExamenFaltante.upper()) + ".")


#PARA BUSCAR PACIENTE Y OBTENER SUS DATOS Y SUS EXAMENES
def obtenerDatosPaciente(paciente):
    # print("SE INGRESA AL METODO obtenerDatosPaciente")
    if paciente in archivoPacientes:
        # print("Nombre paciente: " + paciente + " Examenes: " + str(archivoPacientes[paciente]))
        return archivoPacientes[paciente]

#PARA BUSCAR HORAS Y SI PACIENTE SE PUEDE ATENDER
# def revisarHoraPaciente(paciente):
#     # print("SE INGRESA AL METODO revisarHoraPaciente")
#     imprimirHorasDisponibles(diccionarioDisponibilidad) 
#     examenNoDisponible = ""
    # print("Se ha atendido con éxito a " + str(paciente.upper()))
    # print("No es posible atender a " + str(paciente.upper()) + "porque no existen horas disponibles para el examen " + str(examenNoDisponible.upper()) + ".")


def agregarHorasExamen(examenes):
    for key in diccionarioDisponibilidad.keys():
        for exam in examenes:
            if key == exam:
                diccionarioDisponibilidad[key.strip()] = diccionarioDisponibilidad[key.strip()]+1
    # imprimirHorasDisponibles(diccionarioDisponibilidad)

accionIngresada = " "
while accionIngresada != "STOP":
    imprimirHorasDisponibles(diccionarioDisponibilidad)
    accion = input("Bienvenido, ingrese la instrucción a continuación: ")
    opcionIngresada = accion.split(" ")
    accionIngresada = opcionIngresada[0].upper()
    # print(nombrePaciente)
    if accionIngresada == "STOP":
        # print("accion STOP")
        break
    elif accionIngresada == "AGREGAR":
        examenes = []
        examenesParaAgregar = accion.lstrip("agregar ")
        examenes = examenesParaAgregar.split(" ")
        # print("EXAMENES PARA AGREGAR: " + str(examenes))
        agregarHorasExamen(examenes)
        # print("EXAMENES PARA AGREGAR: " + examenesParaAgregar)
        # print("accion agregar")
    elif accionIngresada == "ATENDER":
        nombrePaciente = opcionIngresada[1].capitalize()
        # obtenerDatosPaciente(nombrePaciente)
        calculoHorasDisponibles(nombrePaciente)
        # revisarHoraPaciente(nombrePaciente)        
        # print("Accion atender")

