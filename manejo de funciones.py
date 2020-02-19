PI = 3.141516
#Area del cuadrado
def acuadrado():
    lado = int(input("Cual es el valor del lado?"))
    x = lado**2
    print("\nEl area del cuadrado es ", x, "unidades cuadradas")

def atriangulo():
    base = int(input("Cual es el valor de la base? "))
    altura = int(input("Cual es el valor de la altura? "))
    y = base*altura
    print("\nEl area del triangulo es ", y, "unidades cuadradas")
    
def acirculo():
    radio = int(input("Cual es el valor del radio? "))
    z= (PI*radio)**2
    print("\n El area del circulo es ", z, "unidades cuadradas")
    
    
i = True
while i==True:
    area=int(input("\n Elije la figura geometrica a calcular su area \n 1. cuadrado \n 2. triangulo \n 3. circulo \n"))
    if area == 1:
        acuadrado()
    elif area == 3:
        acirculo()
    elif area == 2:
        atriangulo()
    else:
        print("\n Ingresa una opcion valida")
    i = bool(input("\n quieres hacer otro calculo?\n si= True \n no=False"))
    