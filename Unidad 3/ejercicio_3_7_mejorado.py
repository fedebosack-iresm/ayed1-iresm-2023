"""
### **Ejercicio 3.7:**
El programa debe:
*   Mostrar al usuario un menu
*   Permitir al usuario ingresar una opcion del menu
*   imprimir esa opcion
*   en caso de no escribir ninuna opcion del menu indicar ERROR

Condiciones:

1.   imprimir (string)
2.   1 (int)
3.   2 (int)
4.   salir (string)

Ayuda (como se comparan string y enteros **cuidado** con castear antes de verificar si el usuario ingreso str o int)
"""
menu = """
MENU BANCO
1.   Extraer dinero
2.   Ingresar dinero
3.   Depositos
4.   salir

opcion: """
flag = True
while flag:
    opcion = input(menu)
    match opcion:
        case '1':
            print('Extraer de dinero')
        case '2':
            print('Ingrear de dinero')
        case '3':
            print('Deposita dinero')
        case '4':
            print('Saliendo')
            flag=False
        case _:
            print('opcion incorrecta')