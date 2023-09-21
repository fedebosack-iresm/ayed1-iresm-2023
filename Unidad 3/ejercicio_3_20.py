"""
###**Ejercicio 3.20**
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    pedir al usuario la duracion en minutos de cada tramo
*    calcular el tiempo total de viaje
*    no deben generar errores"""
while True:
    try:
        tramos = int(input("Ingrese la cant de tramos: "))
        break
    except Exception as e:
        print(e)

duracion_total = 0
for i in range(tramos):
    while True:
        try:
            duracion_total += float(input(f'Ingrese la duracion del tramo {i+1}: '))
            break
        except Exception as e:
            print('El valor debe ser un numero!!!')
print(f"Tiempo total de viaje: {duracion_total}")