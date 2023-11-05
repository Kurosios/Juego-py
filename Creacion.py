import Nivel as lv
import Habilidad as hb
import Inventario as bag
import Equipo as eq
class Personaje :
    def __init__ (self):
        self.nivel = lv.Level()
        self.habilidad = hb.Habilidades()
        self.vida = self.habilidad.constitucion.vida
        self.inventario = bag.Bag()
        self.equipo = eq.Equipo ()
