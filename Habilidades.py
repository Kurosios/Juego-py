from abc import ABC, abstractclassmethod

class Habilidad (ABC):
    @abstractclassmethod
    def sumar_puntos (self,puntos):
        pass
    def informacion (self):
        pass

class Fuerza (Habilidad) :
    def __init__ (self):
        self.nivel = 1
        self.dmgfisico = 1 * self.nivel

    def sumar_puntos (self,puntos):
        self.nivel += puntos
        self.dmgfisico = self.nivel * 2
    def informacion (self):
        return f'Puntos: {self.nivel}, Daño: {self.dmgfisico}'
        
        
class Agilidad (Habilidad):
    def __init__ (self):
        self.nivel = 1
        self.velocidad = 1 * self.nivel
        self.reflejos = 1 * self.nivel
        
    def sumar_puntos (self,puntos):
        self.nivel += puntos
        self.reflejos = self.nivel * 2
        self.velocidad = self.nivel * 1
    def informacion (self):
        return f'Puntos: {self.nivel}, Reflejos: {self.reflejos}, Velocidad: {self.velocidad}'
        
        
class Magia (Habilidad):
    def __init__ (self):
        self.nivel = 1
        self.dmgmagic = 1 * self.nivel
        
    def sumar_puntos (self,puntos):
        self.nivel += puntos
        self.dmgmagic = self.nivel * 2
    def informacion (self):
        return f'Puntos: {self.nivel}, Daño Magico: {self.dmgmagic}'

        
class Constitucion (Habilidad):
    def __init__ (self):
        self.nivel = 1
        self.vida = 2 * self.nivel
        self.resistencia = 1 * self.nivel
        
    def sumar_puntos (self,puntos):
        self.nivel += puntos
        self.vida = self.nivel * 2
        self.resistencia = self.nivel * 1
    def informacion (self):
        return f'Puntos: {self.nivel}, Vida: {self.vida}, Resistencia: {self.resistencia}'
        

class Carisma (Habilidad):
    def __init__ (self):
        self.nivel = 1
        self.persuasion = 1 * self.nivel
        self.suerte = 1 * self.nivel
        
    def sumar_puntos (self,puntos):
        self.nivel += puntos
        self.persuasion = self.nivel * 2
        self.suerte = self.nivel * 1
    def informacion (self):
        return f'Puntos: {self.nivel}, Persuasion: {self.persuasion}, Suerte: {self.suerte}'
        
        
class Inteligencia (Habilidad):
    def __init__ (self):
        self.nivel = 1
        self.logica = 1 * self.nivel
        self.hab_magica = 1 * self.nivel

    def sumar_puntos (self,puntos):
        self.nivel += puntos
        self.logica = self.nivel * 2
        self.hab_magica = self.nivel * 1
    def informacion (self):
        return f'Puntos: {self.nivel}, Logica: {self.logica}, Habilidad Magica: {self.hab_magica}'

class Habilidades :
    def __init__(self):
        self.fuerza = Fuerza()
        self.agilidad = Agilidad()
        self.magia = Magia()
        self.constitucion = Constitucion()
        self.carisma = Carisma()
        self.inteligencia = Inteligencia()
    
    def informacion (self):
        return f'Fuerza: {self.fuerza.informacion()}\nAgilidad: {self.agilidad.informacion()}\nMagia: {self.magia.informacion()}\nConstitucion: {self.constitucion.informacion()}\nCarisma: {self.carisma.informacion()}\nInteligencia: {self.inteligencia.informacion()}\n'

