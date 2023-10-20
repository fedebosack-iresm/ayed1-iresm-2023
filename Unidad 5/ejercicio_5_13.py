'''
##**Ejercicio 5.13**
Crear una funcion que debe: (usar diccionario)
*   Guardar en un diccionario los precios de las frutas de la tabla.
*   Preguntar al usuario por una fruta, un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta.
*   Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.

| Fruta | Precio|
|:-|:-:|
|banana | 50 |
|manzana | 80|
|pera| 100|
|naranja | 30|
'''
diccionario = {
    'banana': 50,
    'manzana': 60,
    'pera': 100,
    'naranja': 30
}

def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int


fruta = input('ingrese una fruta: ')
if(fruta in diccionario.keys()):
    kg = pedir_un_int('ingrese un numero de kilos: ')
    print(f'El total a pagar es: {kg*diccionario.get(fruta)}')
else:
    print('la fruta es incorrecta! ')