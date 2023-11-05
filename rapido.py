import random


class Bag:
    def __init__ (self):
        self.inventario = []
        self.imax = 7
        self.total = 0
    def agregar (self,item):
        if self.total + 1 <= 8:
            self.total += 1
            self.inventario.append(item)
            print("el item fue recogido")
        else :
            print("la mochila va llena")
    def reco (self):
        for i in self.inventario :
            print (i)
    def quitar (self,item):
        if self.total > 0:
            for e in self.inventario:
                if e == item:
                    self.inventario.remove(e)
                    self.total -= 1
                    print ("se quito el elemento exitosamente")
                    break
            else:
                print ("el elemento no se encontro")


class Equipo:
    def __init__ (self):
        self.inventario = []
        self.imax = 2
        self.total = 0 
        
    def desequipar (self,mochila,item):
        if mochila.agregar:
            for i in self.inventario:
                if i == item:
                    mochila.agregar(i)
                    self.inventario.remove(i)
        else:
            print ("no hay lugar en el inventario")
    

    def ver (self):
        for i in self.inventario :
            print (i)
            
    def equipar (self,mochila,item):
        for i in mochila.inventario:
            if i == item:
                if self.total + 1 < 2:
                    self.inventario.append(i)
                    mochila.quitar(i)
                    self.total += 1
                    print ("se equipo correctamente")

                else:
                    print("equipamiento lleno")

class Habilidad :
    def __init__ (self):
        self.fuerza = 1
        self.vida = 400
    def aumentar_str (self,puntos):
        self.fuerza = self.fuerza + (4 * puntos)
    def aumentar_vida (self,puntos):
        self.vida = 400 + (puntos * 40 )

    def descr (self):
        return f'Fuerza: {self.fuerza}\nVida: {self.vida}\n'

class Level :
    def __init__ (self):
        self.nivel = 1
        self.exp = 1

    def subir_nivel (self,aumentar):
        self.nivel +=  aumentar

    def subir_exp (self,exp):
        self.exp += exp
        
    def comprobar (self):
        a = 0
        while self.exp > 100 and self.nivel < 30:
            self.subir_nivel(1)
            self.exp -= 100   
            a += 1
        return a

        
        
    def info (self):
        return f'Nivel: {self.nivel}\nRango: {self.rango}\nExperiencia: {self.exp}'
class Personaje : 
    def __init__ (self,nombre):
        self.nombre = nombre 
        self.nivel = Level()
        self.habilidad = Habilidad()
        self.mochila = Bag()
        self.equipo = Equipo()
        self.puntos = 5
        self.vida = self.habilidad.vida
        
    def descontar_vida (self,daño):
        self.vida -= daño
        print (self.vida)

    def aumentar_hab (self,hab):
        if self.puntos:
            match hab:
                case "str":
                    self.habilidad.aumentar_str(self.puntos)
                    self.puntos = 0
                    print(f"se subio la fuerza correctamente. Fuerza: {self.habilidad.fuerza}")
                case "life":
                    self.habilidad.aumentar_vida(self.puntos)
                    self.puntos = 0
                    print(f"se subio la fuerza correctamente. Vida: {self.habilidad.vida}")
                case _:
                    print ("no existe esa habilidad")
    def subir_puntos (self):
        self.puntos = self.puntos + self.nivel.comprobar()
    def descripcion (self):
        return f'{self.nombre}, vida: {self.vida}'

class Mons :
    def __init__ (self,nombre,fuerza,vida):
        self.nombre = nombre
        self.fuerza = 2 * fuerza
        self.vida = 500 + (vida * 10)
    
    def descontar_vida (self,daño):
        self.vida -= daño
        print (self.vida)


    def info (self):
        return f'Nombre: {self.nombre}\n Vida: {self.vida}'
 

def tirar_dados(desc):
    if desc == "Si":
        numero = random.randint(1,20)
        return numero
    else:
        return -1

def tirada (numero):
    if numero != -1:
        if numero > 10 : 
            mult = numero %10
            dmg = 20 * mult 
            print(f"aumento {mult}")
        else:
            mult = numero /10
            dmg = 20 * mult
            print(f"reducio {mult}")
        return dmg
    else:
        return 100

p1 = Personaje("Pichon")
ene = Mons("Dagarraco",p1.nivel.nivel,p1.nivel.nivel)
      
decision = "no"

dmg = tirada(tirar_dados(decision))

print (dmg)

if dmg != 100:
    daño = dmg
else:
    daño = p1.habilidad.fuerza
    

print(daño)

while ene.vida > 0 and p1.vida > 0:
    a = random.randint(1,100)
    if a > 50:
        ene.descontar_vida(daño):
        print(ene.info())
        print(p1.descripcion())
    else:
        p1.descontar_vida(ene.fuerza)
        print(ene.info())
        print(p1.descripcion())

print(ene.info())
print(p1.descripcion())
