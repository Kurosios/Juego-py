from abc import ABC, abstractclassmethod
class Items(ABC):
    @abstractclassmethod
    def __init__(self,nombre,peso,algo):
        self.nombre = nombre
        self.peso = peso
        self.descripcion = algo


    def Informacion(self):
        return f'Nombre: {self.nombre} \n Peso: {self.peso} \n Descripcion: {self.descripcion}'
    
class Armas (Items):
    def __init__ (self,nombre,peso,descripcion,tipo,dmg):
        super().__init__(nombre,peso,descripcion)
        self.tipo = tipo
        self.dmg = dmg
    
    def descripcion_armas (self):
        return f'{self.tipo} \n {self.Informacion()} \n Daño: {self.dmg} \n '
        
class Armadura (Items):
    def __init__ (self,nombre,peso,descripcion,parte,armor):
        super().__init__(nombre,peso,descripcion)
        self.parte = parte
        self.armor = armor
    
    def descripcion_armadura (self):
        return f'{self.parte} \n {self.Informacion()} \n Armor: {self.armor} \n '
        
class Pocion (Items):
    def __init__ (self,nombre,peso,descripcion,efecto,cantidad):
        super().__init__(nombre,peso,descripcion)
        self.efecto = efecto
        self.cant = cantidad
    
    def descripcion_pociones (self):
        return f'{self.Informacion()} \n Efecto: {self.efecto} \n Cantidad: {self.cant} \n'