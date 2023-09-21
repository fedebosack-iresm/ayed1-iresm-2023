"""
#### **Ejercicio 3.1**
El programa debe:
*   pedir el ingreso de un número positivo al usuario y almacenar la respuesta en la variable ```numero```.
*   Verificar que se trate de un numero entero y mostrar un error
*   Comprobar si el número es negativo. Si lo es, el programa debe avisar que no era eso lo que se había pedido. (si no hay error)
*   Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
"""
try:
    numero = int(input('Ingrese un numero positivo: '))
    if numero < 0:
        print(f'El numero: {numero} es negativo')
    
    print(f'El numero es {numero}')
except Exception as e:
    print(f'Error: {e}')