import mysql.connector as db


mydb = db.connect(
host = 'localhost',
user = 'XXXXX',
passwd = 'XXXXX',
database = 'mp2'
)
my_cursor = mydb.cursor()

#Obtener el número de pedidos que ha realizado el cliente con email jessicaflores@example.com
print("INICIO PRIMERA CONSULTA")
print("==========")
print("Obtener el número de pedidos que ha realizado el cliente con email jessicaflores@example.com")
print("==========")
sqlQuerySelect = 'SELECT COUNT(*) \
FROM pedidos aS ped JOIN clientes aS cli \
ON ped.Id_cliente = cli.Id \
WHERE email = "jessicaflores@example.com";'
my_cursor.execute(sqlQuerySelect)
row = my_cursor.fetchone()
print("Total de pedidos realizados: " + str(row[0]))
print("==========")
print("==========")
print("Imprimi por separado cada pedido realizado, no entendi nuevamente si era el total o cada uno")
print("==========")
sqlQuerySelect = 'SELECT ped.id \
FROM pedidos aS ped JOIN clientes aS cli \
ON ped.Id_cliente = cli.Id \
WHERE email = "jessicaflores@example.com";'
my_cursor.execute(sqlQuerySelect)
rows = my_cursor.fetchall()
count = 1
for row in rows:
    total = '{:,}'.format(row[0]).replace(',','.')
    print("Pedido "+ str(count)+": " + str(total))
    count+=1
print("==========")
print("FIN PRIMERA CONSULTA")
print("==========")
print("\n")

#Obtener el id, nombre, precio y cantidad pedida de cada producto solicitado en el pedido con id 2
print("INICIO SEGUNDA CONSULTA")
print("==========")
print("Obtener el id, nombre, precio y cantidad pedida de cada producto solicitado en el pedido con id 2")
print("==========")
sqlQuerySelect = 'SELECT prod.id, prod.nombre, prod.precio, prodped.cantidad \
FROM productos AS prod JOIN productos_pedidos AS prodped \
ON prod.id = prodped.id_producto \
WHERE prodped.id_pedido = 2'
my_cursor.execute(sqlQuerySelect)
rows = my_cursor.fetchall()
columns = [column[0] for column in my_cursor.description]
for row in rows:
    price = '${:,}'.format(row[2]).replace(',','.')
    print(str(columns[0]).upper() + ": " + str(row[0]) + " " + str(columns[1]).upper() + ": " + str(row[1]) + " " + str(columns[2]).upper() + ": " + str(price) + " " + str(columns[3]).upper() + ": " + str(row[3]))
    
print("==========")
print("FIN SEGUNDA CONSULTA")
print("==========")
print("\n")

print("INICIO TERCERA CONSULTA")
print("==========")
print("Obtener el id y nombre de los 3 productos con más unidades vendidas, junto al número total de unidades vendidas.")
print("==========")
sqlQuerySelect = 'SELECT id, nombre, SUM(cantidad) as TOTAL \
FROM productos_pedidos AS prodped JOIN productos AS prod \
ON prod.id = prodped.id_producto \
GROUP BY id_producto  \
ORDER BY TOTAL DESC LIMIT 3'
my_cursor.execute(sqlQuerySelect)
rows = my_cursor.fetchall()
count = 1
for row in rows:
    total = '{:,}'.format(row[2]).replace(',','.')
    print(str(count) +"° producto mas vendido.")
    print("Id: " +str(row[0]))
    print("Nombre: " + str(row[1])) 
    print("Total unidades vendidas: " + str(total) +"\n")
    count+=1
print("==========")
print("FIN TERCERA CONSULTA")
print("==========")
print("\n")