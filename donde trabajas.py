respuesta = input("tienes que manejar para ir al trabajo? ")
if respuesta == "no":
    print("eres afortunado")
if respuesta == "si":
    print("trabajas fuera de casa")
    
    tiempo = int(input("cuantos minutos haces ? "))
    if tiempo <= 15:
        print("no es muy lejos")
    elif  tiempo>15 and tiempo<=45:
        print("queda lejos")