"""
##**Ejercicio 5.12**
Crear una funcion que debe: (usar diccionario)
*   Preguntar al usuario su nombre, edad, dirección y teléfono y lo guardar en un diccionario.
*   Mostrar por pantalla el mensaje:  "nombre" tiene "edad" años, vive en "direccion" y su número de teléfono es "telefono" de todos los datos del diccionario"""
def get_info():
    diccionario_personas = {}
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese la edad: ')
    dirección = input('Ingrese la dirección: ')
    telefono = input('Ingrese el teléfono: ')
    diccionario_personas.update({'nombre':nombre,'edad':edad,'direccion':dirección,'telefono':telefono})
    print(f"- nombre: {diccionario_personas.get('nombre')}\
            - edad: {diccionario_personas.get('edad')}\
            - direccion: {diccionario_personas.get('direccion')}\
            - telefono: {diccionario_personas.get('telefono')}")

get_info()