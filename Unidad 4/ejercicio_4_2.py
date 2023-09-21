"""
###**Ejercicio 4.2 (Mediciones)**
El programa debe:
*   Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),calcular Area (circulo), calcular Perimetro(circulo))
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
# faltan unidades de medida
import math

def cal_area_cuadr(base,altura):
    return base*altura

def cal_perimetro_cuadr(base,altura):
    return 2*base+2*altura

def cal_area_circ(radio):
    return math.pi*math.pow(radio,2)

def cal_perimetro_circ(radio):
    return 2*math.pi*radio

def pedir_dos_lados():
  while True:
    try:
        lado_1 = float(input("Dame el 1° lado: "))
        lado_2 = float(input("Dame el 2° lado: "))
        return lado_1,lado_2
    except Exception as e:
       print('Los argumentos deben ser decimales o enteros')

def pedir_radio():
  while True:
    try:
        radio = float(input("Dame el radio del circulo: "))
        return radio
    except Exception as e:
       print('Los argumentos deben ser decimales o enteros')

def main():
    while True:
        menu = """
        Mediciones 
        1.   Calcular area de un cuadrilatero
        2.   Calcular perimetro de un cuadrilatero
        3.   Calcular area de un circulo
        4.   Calcular perimetro de un circulo
        5.   Salir

        opcion: """
    
        opcion = input(menu)
        match opcion:
            case '1':
                lado_1,lado_2 = pedir_dos_lados()
                print(cal_area_cuadr(lado_1,lado_2))
            case '2':
                lado_1,lado_2 = pedir_dos_lados()
                print(cal_perimetro_cuadr(lado_1,lado_2))
            case '3':
                radio = pedir_radio()
                print(cal_area_circ(radio))
            case '4':
                radio = pedir_radio()
                print(cal_perimetro_circ(radio))
            case '5':
                print('Saliendo')
                return
            case _:
                print('opcion incorrecta')

if __name__ == "__main__":
    main()
