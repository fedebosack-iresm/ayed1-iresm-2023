"""
### **Ejercicio 3.5**
El programa debe :
*    Pedir al usuario un string
*    Determinar si esa cadena esta en minusculas o mayusculas"""
cadena = input("Ingresa una cadena de texto: ")
if(cadena.islower()):
    print('La cadena es todo minuscula')
elif(cadena.isupper()):
    print('La cadena es todo mayuscula')
else:
    print('No es todo minuscula ni mayuscula o contine numeros')