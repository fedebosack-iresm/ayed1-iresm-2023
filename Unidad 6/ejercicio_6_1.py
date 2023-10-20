'''###**Ejercicio 6.1**
Crear una clase de Persona:
*   Cuyo constructutor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad de recidencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolecente (14 a 22), Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)
    
Crear una funcion que permita agregar objectos a una lista'''
class Persona:
    def __init__(self,nombre='',apellido='',edad='',ciudad=''):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
    
    def presentarse(self):
        print(f'Soy {self.nombre} {self.apellido}, tengo {self.edad} años y vivo en {self.ciudad}')

    def get_tipo_persona(self):
        if 0 < self.edad < 14:
            print('soy un niño')
        # completar if else
        
    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

per_1 = Persona('test','test',90,'test')