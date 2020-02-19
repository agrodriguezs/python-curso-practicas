'''
Created on 8 oct. 2019

@author: Adriana
'''
import sqlite3
from pip._vendor.distlib.compat import raw_input

def insertar():
    db1 = sqlite3.connect('novelas.db')
    print("Estas en la funsion insertar")

    nombre1 = raw_input("Escribe el titulo de la novela: ")
    autor1 = raw_input("Escribe el autor de la novela: ")
    year1 = raw_input("Escribe el anio de la novela:  ")
    
    consulta = db1.cursor()
    
    strConsulta = "insert into tabla (nombre, autor, year) values ('" +nombre1+"','" +autor1+ "','" +year1+ "')"
    print(strConsulta)
    
    consulta.execute(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()
    
def consultar():
    db2 = sqlite3.connect('novelas.db')
    print("Estas en la funsion consultar")
    db2.row_factory = sqlite3.Row
    consulta2 = db2.cursor()
    consulta2.execute("Select * from tabla")
    filas = consulta2.fetchall()
    lista = []
    for fila in filas:
        s ={}
        s['nombre'] = fila['nombre']
        s['autor'] = fila['autor']
        s['year'] = fila['year']
       # print(s['nombre']+', '+ s['autor']+', '+ str(s['year']))
        lista.append(s)
        

    consulta2.close()
    db2.close()
    return(lista)

#insertar()

def menu():
    opcion = input("Ingresa la opcion deseada \n 1.- ingresar una novela \n 2.- consultar las novelas\n")
    if int(opcion) == 1:
        insertar()
        menu()
    elif int(opcion) == 2:
        ListaNovelas = consultar()
        for novela in ListaNovelas:
            print(novela['nombre']+', '+ novela['autor']+', '+ str(novela['year']) )
        menu()
menu()