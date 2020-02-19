cadena1 = "La violencia es el ultimo recurso del incompetente"

#cuenta letras
print(cadena1.count("e"))

#cuenta palabras
print(cadena1.count("violencia"))

#minusculas
print(cadena1.lower())

#mayusculas
print(cadena1.upper())

#remplazo de palabras
print(cadena1.replace("recurso","medio",1))

#division de cadenas
print(cadena1.split("o",2))

#cantidad de apariciones de un caracter
print(cadena1.find("v"))

#Busca el caracter  y regresa el índice donde se encuentra.
print(cadena1.rfind("i"))

#concatenacion
l1 = ["A","B","R","A","H","A","M"]
v = "-"
print(v.join(l1))