"""
##**Ejercicio 5.11**
Crear una funcion que debe: (usar diccionario)
*  Contener un diccionario con distintas monedas de paises, siendo:
La key el nombre de la moneda y el valor el simbolo.
*  Preguntar al usuario que tipo de moneda desea y mostrar el simbolo si existe en el diccionario, caso contrario indicar que no existe."""
monedas = {
    "Peso":"$", 
    "Dolar": "USD",
    "Euro":  "€"
    }
def get_simbolo():
    moneda = input('ingrese la moneda a buscar si simbolo: ').capitalize()
    print(monedas.get(moneda,'La moneda no existe en el diccionario'))

get_simbolo()