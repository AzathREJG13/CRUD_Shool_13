import mysql.connector 
from password import password

conexion = mysql.connector.connect(user = 'root', password = password, 
                                   host = 'localhost', database = 'Crud_School', 
                                   port = '3306')

print(conexion)

cursor = conexion.cursor()