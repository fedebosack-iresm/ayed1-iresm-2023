"""
# **Ejercicio 5.6 (Programa de Inventario de verduleria)**
Crear un prgrama que debe:
*    Contar con un stock de frutas y otro de verduras (El stock indica si venden o no esa fruta o verdura, no la cantidad) - usar listas dentro de listas
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock
"""
from funciones import *

def menu():
    while True:
        menu = """
1. Agregar frutas
2. Consultar el stock de frutas
3. Eliminar un elemento del stock
4. Listar tabla
5. Salir

opcion: """
        base_frutas = [['fruta'],['stock']] 
        opcion = input(menu)
        match opcion:
            case '1':
                base_frutas = agregar_stock_frutas(base_frutas)
            case '2':
                consultar_stock(base_frutas)
            case '3':
                base_frutas = eliminar_stock(base_frutas)
            case '4':
                imprimir_base(base_frutas)
            case '5':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()