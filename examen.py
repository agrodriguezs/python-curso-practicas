class Animal:
    def nacer(self):
        print("ha nacido");
    def mover(self):
        print("se mueve con extremidades");
class Pez(Animal):
    def respirar(self):
        print("ha nacido");
    def mover(self):
        print("se mueve con aletas");
        
tiburon = Pez()
tiburon.nacer()