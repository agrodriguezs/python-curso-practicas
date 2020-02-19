class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("\nSe ha creado a ",self.nombre," de ",self.edad," anos de edad \n")

    def hablar(self, *palabras):
        for frase in palabras:
            print(self.nombre,":", frase)
            
class Deportista(Persona):
    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte
        print("\nSe ha creado a ",self.nombre," de ",self.edad," anos de edad \n")
    
    def getDeporte(self):
        return self.__deporte;
        
    def practicarDeporte(self):
        print(self.nombre, ": voy a practicar ", self.getDeporte())
        
juan = Persona(10, "Juan Carlos");
juan.hablar("holaaaa", "bien, y tu que tal?");
luis = Deportista(12, "Luis Guillermo", "tenis de mesa");
luis.hablar("hola", "como estas?")
luis.practicarDeporte()

    