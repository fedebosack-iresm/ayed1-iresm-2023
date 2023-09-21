"""
###**Ejercicio 3.13**
El programa debe:
*   pedir al usuario una palabra
*   pedir un numero al usuario
*   mostrar la palabra por pantalla la cantidad de veces que diga el numero
*   no debe generar errores
"""
palabra = input('Ingrese una palabra: ')
flag = True
while flag:
    try:
        numero = int(input('Ingrese un numero: '))
        flag = False
    except Exception as e:
        print('Debe ingresar un numero')

#print((palabra+'\n') * numero)
cont = 0
while cont < numero:
    print(palabra)
    cont+=1


#tabnine AI