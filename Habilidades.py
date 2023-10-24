class atributos :
    def __init__ (self):
        self.fuerza = 5
        self.agilida = 5

    def seleccionar_habilidad()

    def agregar_puntos (self,puntos,habilidad):
        continuar = "si"
        while continuar == "si":
            
            match habilidad:
                case "fuerza" :
                    subir = int (input("Cuantos puntos va a subir: "))
                    if subir <= puntos:
                        self.fuerza += subir
                        puntos -= subir
                        print(f"se aumento {subir} a fuerza, restan {puntos} por subir" )
                    else:
                        print(f"no se pueden subir los puntos que se ingreso")
                case "agilidad": 
                    subir = int (input("Cuantos puntos va a subir: "))
                    if subir <= puntos:
                        self.agilidad += subir
                        puntos -= subir
                        print(f"se aumento {subir} a agilidad , restan {puntos} por subir" )
                    else:
                        print(f"no se pueden subir los puntos que se ingreso")
                    
                case _: 
                    print("maquinola esa habilidad no existe")
            continuar = input("Si desea seguir agregando punto ingrese si, de lo contrario, ingrese cualquier cosa: ")
 
capo = atributos()
text = input("que habilidad vas a subir?: ")
puntos = int(input("ingrese punto: "))
capo.agregar_puntos(puntos,text)