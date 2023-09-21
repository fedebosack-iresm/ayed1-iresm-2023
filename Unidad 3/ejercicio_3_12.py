"""###**Ejercicio 3.12**
El programa debe:
*  pedir al usuario un número entero del 1 al 9 y muestrar por pantalla la tabla del numero (del 1 al 10).
*  no debe generar errores"""
flag = True
while flag:
    try:
        numero = int(input('Ingrese un numero del 1 al 9: '))
        if(1 <= numero <=9):   
            flag = False
            # salgo del bucle con un numero entre el 1 y 9
        else:
            print('El numero tiene que ser entre el 1 y 9')
    except Exception as e:
        print('ERROR, el dato tiene que ser numerico')

cont = 1
while cont <=10:
    print(f"{numero}x{cont} = {numero*cont}")
    cont+=1
