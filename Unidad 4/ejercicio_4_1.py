"""
###**Ejercicio 4.1 (Calculadora)**
El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores"""

def suma(a,b):
  try:
    suma = float(a)+float(b)
    print(f"la suma de {a} y {b} es: {suma}")
  except:
    print("argumentos malos")

def resta(a,b):
  try:
    resta = float(a)-float(b)
    print(f"la resta de {a} y {b} es: {resta}")
  except:
    print("argumentos malos")

def multiplicacion(a,b):
  try:
    mult = float(a)*float(b)
    print(f"la mult de {a} y {b} es: {mult}")
  except:
    print("argumentos malos")

def division(a,b):
  try:
    division = float(a)/float(b)
    print(f"la division de {a} y {b} es: {division}")
  except:
    print("argumentos malos")

def pedir_dos_argumentos_float(texto_1,texto_2):
  while True:
    try:
        num_1 = float(input(texto_1))
        num_2 = float(input(texto_2))
        return num_1,num_2
    except Exception as e:
       print('Los argumentos deben ser decimales o enteros')

def menu():
    while True:
        menu = """
        CALCULADORA
        1.   sumar
        2.   restar
        3.   multiplicar
        4.   dividir
        5.   Salir

        opcion: """
    
        opcion = input(menu)
        if opcion in ['1','2','3','4']:
           a,b = pedir_dos_argumentos_float('Dame un numero: ','Dame un numero: ')
        match opcion:
            case '1':
                suma(a,b)
            case '2':
                resta(a,b)
            case '3':
                multiplicacion(a,b)
            case '4':
                division(a,b)
            case '5':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()