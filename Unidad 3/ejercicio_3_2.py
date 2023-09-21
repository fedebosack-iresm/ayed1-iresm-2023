"""
####**Ejercicio 3.2**
*Agencia de autos:*

El programa cuenta con tres marcas de autos y su precio.

El programa debe:
*   pedir al usuario que ingrese la cant de dinero que dispone.
*   verificar que la cantidad ingresada sea un numero y sino mostrar error
*   verificar la cantidad de ingresada e indicar que auto o autos puede comprar
"""
precio_ford = 5000
precio_renault = 4000
precio_mercedes = 10000
try:
    dinero_disponible = float(input('Ingrese el dinero disponle: '))
    if dinero_disponible >= precio_mercedes:
        print('Puede comprar un mercedes, renault o ford')
    
    if dinero_disponible >= precio_ford:
        print('Puede comprar un renault o ford')
    
    if dinero_disponible >= precio_renault:
        print('Puede comprar un renault')


except Exception as e:
    print(f'Error: {e}')