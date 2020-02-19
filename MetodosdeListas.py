pi=3.141516
l1 = ["Numero","Letra",[23, pi,278],"variable"]


print((l1).index("variable"))

l1.append("constante")
print(l1)

print((l1).count("variable"))

l1.insert(2,"Valor nuevo")
print(l1)

l2=["Cesar","Mario","Octavio"]
l1.extend(l2)
print(l1)

#Elimina el valor de la lista de acuerdo al índice que elijas.
l1.pop(2)
print(l1)

l1.remove("Numero")
print(l1)

l1.reverse()
print(l1)