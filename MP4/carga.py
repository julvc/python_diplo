from datetime import datetime
import mysql.connector as db
import csv

mydb = db.connect(
host = 'localhost',
user = 'XXXX',
passwd = 'XXXX',
database = 'mp2'
)
my_cursor = mydb.cursor()

#RUTAS CSV
rutaProducto = r"C:\Users\julia\Documents\CURSOS\DIPLOMADO PYTHON CIENCIA DATOS\CURSO 3\CLASE 4\productos.csv"
rutaClientes = r"C:\Users\julia\Documents\CURSOS\DIPLOMADO PYTHON CIENCIA DATOS\CURSO 3\CLASE 4\clientes.csv"
rutaPedidos = r"C:\Users\julia\Documents\CURSOS\DIPLOMADO PYTHON CIENCIA DATOS\CURSO 3\CLASE 4\pedidos.csv"
rutaPedidosProducto = r"C:\Users\julia\Documents\CURSOS\DIPLOMADO PYTHON CIENCIA DATOS\CURSO 3\CLASE 4\productos_pedidos.csv"

#sqlDate = 'SELECT DATE(NOW())'
#my_cursor.execute(sqlDate)
#row = my_cursor.fetchone()
#if row != None:
#    print(str(row))
#else:
#    print("No existe coneccion a BBDD. No data")

#creacion de tablas
sqlTableProductos = 'CREATE TABLE productos ( \
id INTEGER, \
nombre VARCHAR(255), \
descripcion VARCHAR(255), \
precio INTEGER, \
CONSTRAINT PK_productos PRIMARY KEY(id) \
);'
my_cursor.execute(sqlTableProductos)

sqlTableClientes = 'CREATE TABLE clientes(\
id INTEGER,\
nombre VARCHAR(255),\
email VARCHAR(255),\
CONSTRAINT PK_clientes PRIMARY KEY(id)\
);'
my_cursor.execute(sqlTableClientes)

sqlTablePedidos = 'CREATE TABLE pedidos( \
id INTEGER, \
fecha DATE, \
direccion VARCHAR(255), \
id_cliente INTEGER, \
detalle VARCHAR(255), \
CONSTRAINT PK_pedidos PRIMARY KEY(id), \
CONSTRAINT FK_idCliente FOREIGN KEY (id_cliente) REFERENCES clientes(id));'
my_cursor.execute(sqlTablePedidos)

sqlTableProductosPedidos = 'CREATE TABLE productos_pedidos( \
id_producto INTEGER, \
id_pedido INTEGER, \
cantidad INTEGER, \
PRIMARY KEY (id_pedido, id_producto), \
CONSTRAINT FK_idProducto FOREIGN KEY (id_producto) REFERENCES productos(id),\
CONSTRAINT FK_idPedido FOREIGN KEY (id_pedido) REFERENCES pedidos(id));'
my_cursor.execute(sqlTableProductosPedidos)

#importa data desde CSV
#productos
with open(rutaProducto) as file:
    reader = csv.reader(file, delimiter=',')
    filas = []
    first = next(reader)
    for row in reader:
        #print('Fila agregada')
        #print(row)
        filas.append(tuple([int(row[0]), row[1], row[2], int(row[3])]))
        
sqlInsertProductos = 'INSERT INTO productos(id, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)'
my_cursor.executemany(sqlInsertProductos, filas)
mydb.commit()

#clientes
with open(rutaClientes) as file:
    reader = csv.reader(file, delimiter=',')
    filas = []
    first = next(reader)
    for row in reader:
        #print('Fila agregada')
        #print(row)
        filas.append(tuple([int(row[0]), row[1], row[2]]))
sqlInsertClientes = 'INSERT INTO clientes(id, nombre, email) VALUES (%s, %s, %s)'
my_cursor.executemany(sqlInsertClientes, filas)
mydb.commit()

#pedidos
with open(rutaPedidos) as file:
    reader = csv.reader(file, delimiter=',')
    filas = []
    first = next(reader)
    for row in reader:
        #print('Fila agregada')
        #print(row)
        filas.append(tuple([int(row[0]), datetime.strptime(row[1], '%Y-%m-%d').date(), row[2], int(row[3]), row[4]]))
sqlInsertPedidos = 'INSERT INTO pedidos(id, fecha, direccion,id_cliente, detalle) VALUES (%s, %s, %s, %s, %s)'
my_cursor.executemany(sqlInsertPedidos, filas)
mydb.commit()

#productos_pedidos
with open(rutaPedidosProducto) as file:
    reader = csv.reader(file, delimiter=',')
    filas = []
    first = next(reader)
    for row in reader:
        #print('Fila agregada')
        #print(row)
        filas.append(tuple([int(row[0]), int(row[1]), int(row[2])]))
sqlInsertProductosPedidos = 'INSERT INTO productos_pedidos(id_producto,id_pedido, cantidad) VALUES (%s, %s, %s)'
my_cursor.executemany(sqlInsertProductosPedidos, filas)
mydb.commit()