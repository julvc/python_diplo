import csv

# ARCHIVO HORAS DISPONIBLES
archivoDisponibilidad = open("disponibilidad.txt", "r", encoding="utf-8")
diccionarioDisponibilidad = {}
paciente = ""
nombrePaciente = ""
for linea in archivoDisponibilidad:
    key, value = linea.split(" ")
    diccionarioDisponibilidad[key.strip()] = int(value.strip())

# ARCHIVO PACIENTES
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
    nombreExamenFaltante = ""
    contador = 0
    pacienteTmp = obtenerDatosPaciente(paciente)
    pacienteAtendido = True
    for key in diccionarioDisponibilidad.keys():
        for pac in pacienteTmp:
            if key == pac:
                if diccionarioDisponibilidad.get(key) > 0:
                    contador+=1
                else:
                    pacienteAtendido = False
                    nombreExamenFaltante = key
    
    if contador == len(pacienteTmp):
        for key in diccionarioDisponibilidad.keys():
            for pac in pacienteTmp:
                if key == pac:
                    if diccionarioDisponibilidad.get(key) > 0:                    
                        diccionarioDisponibilidad[key.strip()] = diccionarioDisponibilidad[key.strip()] -1
                    else:
                        pacienteAtendido = False
    else:
        print("No es posible atender a " + str(paciente.upper()) + " porque no existen horas disponibles para el examen " + str(nombreExamenFaltante.upper()) + ".")
    if pacienteAtendido == True:
        print("Se ha atendido con éxito a " + paciente.upper() +"!")

#PARA BUSCAR PACIENTE Y OBTENER SUS DATOS Y SUS EXAMENES
def obtenerDatosPaciente(paciente):
    if paciente in archivoPacientes:
        return archivoPacientes[paciente]

def agregarHorasExamen(examenes):
    for key in diccionarioDisponibilidad.keys():
        for exam in examenes:
            if key == exam:
                diccionarioDisponibilidad[key.strip()] = diccionarioDisponibilidad[key.strip()]+1

accionIngresada = " "
while accionIngresada != "STOP":
    imprimirHorasDisponibles(diccionarioDisponibilidad)
    accion = input("Bienvenido, ingrese la instrucción a continuación: ")
    opcionIngresada = accion.split(" ")
    accionIngresada = opcionIngresada[0].upper()
    if accionIngresada == "STOP":
        break
    elif accionIngresada == "AGREGAR":
        examenes = []
        examenesParaAgregar = accion.lstrip("agregar ")
        examenes = examenesParaAgregar.split(" ")
        agregarHorasExamen(examenes)
    elif accionIngresada == "ATENDER":
        nombrePaciente = opcionIngresada[1].capitalize()
        calculoHorasDisponibles(nombrePaciente)

