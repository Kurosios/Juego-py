import Nivel as lv
import Habilidad as hb
import Inventario as bag

class Personaje :
    def __init__ (self):
        self.nivel = lv.Level()
        self.habilidad = hb.Habilidades()
        self.vida = self.habilidad.constitucion.vida
        self.inventario = bag.Bag()



p = Personaje()

print(p.Nivel.info())
print(f'Vida: {p.Vida}')
print(p.habilidad.informacion())
print(p.inventario.bag.ver_mochila())