class Hab:
    def __init__  (self,fuerza):
        self.fuerza = fuerza

class Acciones:
    def __init__ (self,descripcion,efecto,cuanto,turnos):
        self.descripcion = descripcion
        self.efecto = efecto 
        self.cuanto = cuanto 
        self.turnos = turnos 

class Item :
    def __init__ (self,nombre,accion):
        self.nombre = nombre 
        self.accion = Acciones()


def consumir (self,item,hab):
    


des = "Por 3 turnos, desde que se consume, aumenta la fuerza un 20% mas"

Str = Hab (800)
acc = Acciones(des,"aumento",20,3)
Vida = Item ("Pocion de vida ")

a = 1 

j = 200000
while a < 10:

    if a == 3 :




