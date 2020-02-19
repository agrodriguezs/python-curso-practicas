class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("\nSe ha creado a ",self.nombre," de ",self.edad," anos de edad \n")

    def hablar(self, **palabras):
        for frase in palabras:
            print(self.nombre,": ", palabras[frase])
juan = Persona(10, "Juan Carlos");
juan.hablar(t1 = "holaaaa", t2 = "bien, y tu que tal?");
luis = Persona(12, "Luis Guillermo");
luis.hablar(t1 = "hola", t2 = "como estas?")

    