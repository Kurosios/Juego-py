class Level :
    def __init__ (self):
        self.nivel = 1
        self.rango = "B"
        self.exp = 1

    def subir_nivel (self,aumentar):
        self.nivel +=  aumentar

    def subir_exp (self,exp):
        self.exp += exp
        
    def comprobar (self):
        while self.exp > 100 and self.nivel < 30:
            self.subir_nivel(1)
            self.exp -= 100
        if self.nivel > 15 and self.nivel < 30:
            self.rango = "A"
        elif self.nivel == 30:
            self.rango = "S"            

        
        
    def info (self):
        return f'Nivel: {self.nivel}\nRango: {self.rango}\nExperiencia: {self.exp}'

