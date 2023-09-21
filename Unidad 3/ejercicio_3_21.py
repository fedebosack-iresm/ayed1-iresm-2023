"""###**Ejercicio 3.21**
El programa debe:
*   Pedir al usuario una palabra
*   Verificar que sea una palabra y no un numero
*   Mostrar por pantalla las letras una a una
*   No producir errores"""
while True:
    palabra = input('Ingrse una palabra: ')
    if palabra.isalpha():
        for letra in palabra:
            print(letra)
        break
    else:
        print('Debe ser una palabra!!!')