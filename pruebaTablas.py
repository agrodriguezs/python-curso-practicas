import sqlite3

conexion = sqlite3.connect('novelas.db')
consulta = conexion.cursor()
tabla = "CREATE TABLE tabla ("\
      "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
      "nombre VARCHAR(30) NOT NULL,"\
      "autor VARCHAR(40) NOT NULL,"\
      "year INTEGER(9) NOT NULL)"

print(tabla)

if (consulta.execute(tabla)):
	print("la tabla fue creada")
else:
	print("la tabla NO fue creada")

consulta.close()
conexion.commit()
conexion.close()