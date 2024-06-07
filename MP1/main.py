import csv
# Parte 1: Cargar los datos
def cargar_datos(lineas_archivo):
    # Completar
    generoTmp = []
    pelisTmp = []
    valueTmp = []
    generos_peliculas = []
    peliculas_por_genero = []
    pelisTuple = tuple()
    pelisList = []
    infoTuple = ()
    info_peliculas = []
    
#OBTENCION DE NOMBRE PELICULAS POR GENERO
    for pelis in lineas_archivo:
        pelisTmp = pelis.split(",")
        listado_genero = [pelisTmp[4].replace(";",",")]
        #print(pelisTmp[0],pelisTmp[1],pelisTmp[2],pelisTmp[3],listado_genero)
        infoTuple = (pelisTmp[0],pelisTmp[1],pelisTmp[2],pelisTmp[3],listado_genero)
        info_peliculas.append(infoTuple)
        print(info_peliculas)

    print(info_peliculas)

#OBTENCION DE GENEROS DE PELICULAS
    for genero in lineas_archivo:
        generoTmp = genero.split(",")
        valueTmp = generoTmp[4].split(";")
        for var in valueTmp:
            if var not in generos_peliculas:
                generos_peliculas.append(var)

#OBTENCION DE NOMBRE PELICULAS POR GENERO
    for genero in generos_peliculas:
        for pelis in lineas_archivo:
            pelisTmp = pelis.split(",")
            listado_genero = [pelisTmp[4].replace(";",",")]
            for generos in listado_genero:
                if genero in generos:
                    if pelisTmp[0] not in pelisList:
                        pelisList.append(pelisTmp[0])
        pelisTuple = (genero,pelisList)    
        print("pelituple: " , pelisTuple) 
        peliculas_por_genero.append(pelisTuple)
    
    print(peliculas_por_genero)
                

    #for pelisPorGenero in lineas_archivo:
    #    #print("lineas archivo1Star Wars: The Last Jedi,44.365,6.8,13984,Adventure;Action;Science Fiction" )
    #    for genero in generos_peliculas:
    #        print("LARGO DE GENEROS PELICULAS " + str(len(generos_peliculas)))
    #        pelisTmp = pelisPorGenero.split(",")
    #        if genero in pelisTmp[4]:
    #            print("genero: " + genero + " nombre peli: " + pelisTmp[0] + " generos sin agrupar: " + pelisTmp[4])
        
        
#genero: Adventure nombre peli: Star Wars: The Last Jedi generos sin agrupar: Adventure;Action;Science Fiction
#genero: Action nombre peli: Star Wars: The Last Jedi generos sin agrupar: Adventure;Action;Science Fiction
        
        
    #lista de peliculas por genero          
        #for index,value in enumerate(valueTmp, start=0):
        #    if value[index] not in generos_peliculas:
        #        generos_peliculas.append(value[index])
        #        print(generos_peliculas)
            
        #for value in generoTmp[4]:
        #    print(value)
            
        #    valueTmp = []
        #    valueTmp = value[4].split(";")            
        #    print(valueTmp)            
        #    for var in valueTmp:
        #        if var not in generos_peliculas:
        #            generos_peliculas.append(var)
        #            print(generos_peliculas)
        
        
        #posicion = str(genero.rfind(','))
        #generoTmp = genero.slice(posicion)
        #print(generoTmp)
        ##print("GENERO OBTENIDO: " + str(genero[posicion:]))
        ##generos_peliculas.append(genero[posicion:])
        # print("genero_split: " + genero_split[1]) 
        # generos_peliculas.append(genero_split[1])
        
        
    #lista de tuplas (genero,[pelicula])
    
    #lista de tuplas (titulo,popularidad,voto_promedio,cantidad_votos,[generos])
    
    pass


# # Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    pass


def filtrar_y_ordenar(genero_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    pass


def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    pass











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
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
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
