"""### **Ejercicio 3.17**
El programa debe:
*    Preguntar al usuario por una frase y una letra
*    mostrar por pantalla el número de veces que aparece la letra en la frase."""

frase = input('digame una frase: ')
letra = input('digame una letra: ')

cont = 0 #inicializo contador
for i in frase:
    if i == letra:
        cont+=1

print(f'La letra {letra} aparece {cont} veces')