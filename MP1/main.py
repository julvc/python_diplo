
generos_peliculas = []
peliculas_por_genero = []
info_peliculas = []

# Parte 1: Cargar los datos
def cargar_datos(lineas_archivo):
    pelisTuple = tuple()
    infoTuple = ()
    generoTmp = []
    pelisTmp = []
    valueTmp = []

#OBTENCION DE GENEROS DE PELICULAS
    for genero in lineas_archivo:
        generoTmp = genero.split(",")
        valueTmp = generoTmp[4].split(";")
        for var in valueTmp:
            if var not in generos_peliculas:
                generos_peliculas.append(var)

#OBTENCION DE NOMBRE PELICULAS POR GENERO
    for genero in generos_peliculas:
        pelisList = []
        for pelis in lineas_archivo:
            pelisTmp = pelis.split(",")
            listado_genero = [pelisTmp[4].replace(";",",")]
            #print(listado_genero)
            for generos in listado_genero:
                if genero in generos:
                    #print("genero: " , genero)
                    #print("pelisTmp[0]: " , pelisTmp[0])
                    if pelisTmp[0] not in pelisList:
                        #print("pelisTmp[0]: " , pelisTmp[0])
                        #print("antes de append: " , pelisList)
                        pelisList.append(pelisTmp[0])
                        #print("despues de append: " , pelisList)
                        #break
        
        pelisTuple = (genero,pelisList)    
        #print("pelituple: " , pelisTuple) 
        peliculas_por_genero.append(pelisTuple)

#OBTENCION DE OTROS DATOS DE PELICULAS
    for pelis in lineas_archivo:
        pelisTmp = pelis.split(",")
        listado_genero = pelisTmp[4].split(";")
        infoTuple = (pelisTmp[0],pelisTmp[1],pelisTmp[2],pelisTmp[3],listado_genero)
        info_peliculas.append(infoTuple)

    #retorna objetos creados
    tuplaFinal = (generos_peliculas,peliculas_por_genero,info_peliculas)
    return tuplaFinal


# Parte 2: Completar las consultas
#obtener_puntaje_y_votos(nombre_pelicula): Esta función recibe un
#string, que corresponde al nombre de una película y debe retornar una
#tupla, donde el primer elemento debe ser el puntaje promedio de la
#película y el segundo elemento debe ser la cantidad de votos que tiene.

#titulo,popularidad,voto_promedio,cantidad_votos,generos
def obtener_puntaje_y_votos(nombre_pelicula):
    result = tuple()
    for value in info_peliculas:
        if nombre_pelicula in value:
            result = (value[2], value[3])
    return result


def filtrar_y_ordenar(genero_pelicula):
    result = []
    #[item for item in a if item[0] == 1]
    #[item for item in a if 1 in item]
    for value in peliculas_por_genero:
        if genero_pelicula in value:
            result = sorted(value[1], reverse=True)
            break

    return result

def obtener_estadisticas(genero_pelicula, criterio):
    popularidad_list = []
    votoPromedio_list = []
    cantidadVotos_list = []
    result = []
    
    if str(criterio).lower() == "popularidad":
        for popularity in info_peliculas:
            if genero_pelicula in popularity[4]:
                popularidad_list.append(eval(popularity[1]))
    elif str(criterio).lower() == "voto promedio":
        for votoPromedio in info_peliculas:
            if genero_pelicula in votoPromedio[4]:
                votoPromedio_list.append(eval(votoPromedio[2]))
    elif str(criterio).lower() == "cantidad votos":
        for votos in info_peliculas:
            if genero_pelicula in votos[4]:
                cantidadVotos_list.append(eval(votos[3]))
    
    if len(popularidad_list) > 0:
        minValue = min(popularidad_list)
        maxValue = max(popularidad_list)
        averValue = sum(popularidad_list)/len(popularidad_list)
        #result = [round(maxValue), round(minValue), round(averValue)]
        result = [maxValue, minValue, round(averValue,2)]
        print(result)
    
    if len(votoPromedio_list) > 0:
        minValue = min(votoPromedio_list)
        maxValue = max(votoPromedio_list)
        averValue = sum(votoPromedio_list)/len(votoPromedio_list)
        #result = [round(maxValue,2), round(minValue,2), round(averValue,2)]
        result = [maxValue,minValue,round(averValue,2)]
    
    if len(cantidadVotos_list) > 0:
        minValue = min(cantidadVotos_list)
        maxValue = max(cantidadVotos_list)
        averValue = sum(cantidadVotos_list)/len(cantidadVotos_list)
        #result = [round(maxValue), round(minValue), round(averValue)]
        result = [maxValue,minValue,round(averValue,2)]
    
    return result


# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    rutaArchivo = "C:/Users/julia/Downloads/peliculas.csv"
    with open(rutaArchivo, "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
