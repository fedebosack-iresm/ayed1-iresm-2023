"""
### **Ejercicio 3.4**
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario coincide o no con la variable
    **IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
"""

constrasenia = 'Iresm2023'
contrasenia_instroducida = input('Ingrese la constraseña: ')

if(constrasenia.lower() == contrasenia_instroducida.lower()):
    print('Constraseña correcta!!!')
else:
    print('Constraseña incorrecta!!!')

