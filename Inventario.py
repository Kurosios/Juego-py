class Bag:
    def __init__ (self):
        self.inventario = []
        self.peso = 0 
        self.max = 50.0
    
    def agregar_elemento (self,elem):
        if self.peso + elem.peso <= self.max :
            self.peso += elem.peso
            self.inventario.append(elem)
            print('se agrego correctamente el item')
        else:
            print ('la mochila va llena')
    
    
    def imprimir_inventario(self):
        for elemento in self.inventario:
            print (f'Elemento \n Nombre: {elemento.nombre}\n Peso: {elemento.peso}')
        
    def ver_mochila (self):
        return f'{self.imprimir_inventario()} chica \n Peso: {self.peso} \n Peso max: {self.max}'
        
    def borrar_item (self, item):
        self.peso -= item.peso
        self.inventario.remove(item)
        

        
