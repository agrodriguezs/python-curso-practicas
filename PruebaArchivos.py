def escritura(datoa,datob,datoc):
    prueba=open("ArchivoGenerado.py","w")
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print( "Escritura")
    prueba.close()
    
def lectura():
    prueba=open("ArchivoGenerado.py","r")
    print(prueba.read())
    prueba.close()
#escritura("Hola ", "Mundo ", "Querido ")
    
lectura()