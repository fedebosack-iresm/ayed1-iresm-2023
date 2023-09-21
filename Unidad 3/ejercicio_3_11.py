"""###**Ejercicio 3.11 (Tarea)**
El programa debe:
*  pedir al usuario 5 datos numericos
*  verificar que sean enteros y sino pedir nuevamente los 5
*  cuando se tenga los 5 datos el programa debe devolver el promedio
*  no deben aparecer errores."""
flag = True
cont = 0
acumulador = 0
while(flag):
    try:
        acumulador += int(input(f'Escribe el valor {cont+1}: '))
        cont +=1
        if(cont == 5):
            flag = False
            print(f'Promedio = {acumulador/cont}')
    except Exception as e:
        print(e)
        cont = 1
        acumulador = 0