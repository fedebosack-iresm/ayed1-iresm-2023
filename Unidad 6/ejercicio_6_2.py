"""
###**Ejercicio 6.2**
Crear una clase de FiguraGeometrica:
*   Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño (por defecto "pequeño")
*   Se deben crear 3 metodos en la clase:
    1.  Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
    2.  Cambiar color de figura e indicar nuevo color
    3.  verificar si la figura es tamaño pequeño, agrandar a tamaño grande"""

class FiguraGeometrica:
    def __init__(self,tipo_de_figura,color,tamanio='pequeño'):
        self.tipo_de_figura = tipo_de_figura
        self.color = color
        self.tamanio = tamanio

    def verificar_tamanio(self):
        if(self.tamanio == 'pequeño'):
            self.tamanio = 'grande'
        else:
            print('el tamaño no es pequeño')

    def presentarse(self):
        print(f'Es un {self.tipo_de_figura} de color {self.color} y tamanio {self.tamanio}')
 
    def cambiar_color(self):
        color = input('Ingrese el nuevo color: ')
        self.color = color
        print(f'El nuevo color es {self.color}')

# instancio un objeto
figura_1 = FiguraGeometrica('cuadrado','rojo','pequeño')
print(figura_1.color)
