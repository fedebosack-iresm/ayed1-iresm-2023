"""
### **Ejercicio 3.3**
El programa debe :
*   Determinar si una cadena posee sólo números (metodos de string)
"""

cadena = input("Ingresa una cadena de numeros: ")
if (cadena.isnumeric()):
    print('La cadena es numeria')
else:
    print('La cadena no es numerica')