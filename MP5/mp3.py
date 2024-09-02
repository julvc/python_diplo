import pymongo
import requests
import json

#CONEXION A BASE DATOS
client = pymongo.MongoClient("mongodb://localhost:27017/")

#CONFIGURACION ACCESO API
headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
response = requests.get("https://apis.digital.gob.cl/fl/feriados/2024", headers=headers,timeout=10)
resJSON = json.loads(response.text)

#INSERTAR DATOS
mydb = client['feriados']
cursor = mydb['feriados2024']
print("INICIO INSERT FERIADOS")
cursor.insert_many(resJSON)
print("FIN INSERT FERIADOS \n")

#CONSULTAS
#NUMERO 1: Obtener todos los feriados en la colección
print("INICIO CONSULTA 1=================================== Obtener todos los feriados en la colección =====\n")
#for feriados in resJSON: #print desde objeto
#    print(feriados)
collect = cursor.find({},{'_id': 0,'nombre': 1})
print("Solo los nombres de feriados: ")
for c in collect:
    print(c["nombre"])
print("\n")
print("Todos los feriados y sus datos: ")
collect = cursor.find({},{'_id': 0, 'nombre': 1, 'comentarios': 1, 'fecha': 1, 'irrenunciable': 1, 'tipo': 1 })
for c in collect:
    valueIrrenunciable = "Si" if int(c["irrenunciable"]) == 1 else "No"
    print("Nombre feriado: " +c["nombre"] + " Comentarios: " + str(c["comentarios"]) + " Fecha: "+c["fecha"] + " Irrenunciable: " + valueIrrenunciable + " Tipo: " + c["tipo"])
#collect = cursor.find_one({},{'_id': 0, 'nombre': 1, 'comentarios': 1, 'fecha': 1, 'irrenunciable': 1, 'tipo': 1 })
#valueIrrenunciable = "Si" if int(c["irrenunciable"]) == 1 else "No"
print("FIN CONSULTA 1===================================\n")

#NUMERO 2: Obtener solo los feriados de tipo “Religioso”
print("INICIO CONSULTA 2=================================== Obtener solo los feriados de tipo “Religioso”  =====\n")
collect = cursor.find({'tipo': 'Religioso'},{'_id': 0, 'nombre': 1, 'comentarios': 1, 'fecha': 1, 'irrenunciable': 1, 'tipo': 1 })
for c in collect:
    valueIrrenunciable = "Si" if int(c["irrenunciable"]) == 1 else "No"
    print("Nombre feriado: " +c["nombre"] + " Comentarios: " + str(c["comentarios"]) + " Fecha: "+c["fecha"] + " Irrenunciable: " + valueIrrenunciable + " Tipo: " + c["tipo"])
print("\n")
print("FIN CONSULTA 2===================================\n")

#NUMERO 3: Obtener solo los feriados que sean irrenunciables
print("INICIO CONSULTA 3===================================  Obtener solo los feriados que sean irrenunciables =====\n")
collect = cursor.find({'irrenunciable': '1'},{'_id': 0, 'nombre': 1, 'comentarios': 1, 'fecha': 1, 'irrenunciable': 1, 'tipo': 1 })
for c in collect:
    valueIrrenunciable = "Si" if int(c["irrenunciable"]) == 1 else "No"
    print("Nombre feriado: " +c["nombre"] + " Comentarios: " + str(c["comentarios"]) + " Fecha: "+c["fecha"] + " Irrenunciable: " + valueIrrenunciable + " Tipo: " + c["tipo"])
print("\n")
print("FIN CONSULTA 3===================================\n")

#NUMERO 4: Obtener solo los feriados que incluyen el texto “Santo” en su nombre
print("INICIO CONSULTA 4===================================  Obtener solo los feriados que incluyen el texto “Santo” en su nombre =====\n")
collect = cursor.find({'nombre': {'$regex': '.*Santo.*'}},{'_id': 0, 'nombre': 1, 'comentarios': 1, 'fecha': 1, 'irrenunciable': 1, 'tipo': 1 })
for c in collect:
    valueIrrenunciable = "Si" if int(c["irrenunciable"]) == 1 else "No"
    print("Nombre feriado: " +c["nombre"] + " Comentarios: " + str(c["comentarios"]) + " Fecha: "+c["fecha"] + " Irrenunciable: " + valueIrrenunciable + " Tipo: " + c["tipo"])
print("\n")
print("FIN CONSULTA 4===================================\n")

#NUMERO 5: Obtener solo los feriados que se celebran entre el 11 de marzo (2024-03-11) y el 31 agosto (2024-08-31)
print("INICIO CONSULTA 5===================================  Obtener solo los feriados que se celebran entre el 11 de marzo (2024-03-11) y el 31 agosto (2024-08-31) =====\n")
collect = cursor.find({'fecha': {'$gte': '2024-03-11','$lte': '2024-08-31'}},{'_id': 0, 'nombre': 1, 'comentarios': 1, 'fecha': 1, 'irrenunciable': 1, 'tipo': 1 })
for c in collect:
    valueIrrenunciable = "Si" if int(c["irrenunciable"]) == 1 else "No"
    print("Nombre feriado: " +c["nombre"] + " Comentarios: " + str(c["comentarios"]) + " Fecha: "+c["fecha"] + " Irrenunciable: " + valueIrrenunciable + " Tipo: " + c["tipo"])
print("\n")
print("FIN CONSULTA 5===================================\n")

#NUMERO 6:  Insertar un nuevo feriado con las siguientes características
print("INICIO CONSULTA 6===================================   Insertar un nuevo feriado con las siguientes características =====\n")
cursor.insert_one({
    "nombre": "Día de las luces",
"comentarios": None,
"fecha": "2024-03-11",
"irrenunciable": "0",
"tipo": "Religioso"
})

c = cursor.find_one({'nombre': {'$regex': '.*Día de las luces.*'}},{'_id': 0, 'nombre': 1, 'comentarios': 1, 'fecha': 1, 'irrenunciable': 1, 'tipo': 1 })
valueIrrenunciable = "Si" if int(c["irrenunciable"]) == 1 else "No"
print("Nombre feriado: " +c["nombre"] + " Comentarios: " + str(c["comentarios"]) + " Fecha: "+c["fecha"] + " Irrenunciable: " + valueIrrenunciable + " Tipo: " + c["tipo"])
print("\n")
print("FIN CONSULTA 6===================================\n")



