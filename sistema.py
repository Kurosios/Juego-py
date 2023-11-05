import random 


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
        
decision = "Si"


dmg = tirada(tirar_dados(decision))

print (dmg)

if dmg != 100:
    daño = dmg
else:
    daño = p1.habilidad.fuerza
    

