"""
### **Ejercicio 2.3**
El programa debe:
*  pedir por teclado la edad de una persona
*  pedir por teclado los años trabajados
*  devolver los años que le faltan para jubilarse (30 años totales) y a que edad se jubilaria
"""
anios_t_jub = 30
edad = int(input("Indique su edad: "))
anios_trabajados = int(input("Indique los años trabajados: "))
anios_faltantes = anios_t_jub - anios_trabajados
edad_jubilacion = edad + anios_faltantes
print(f'Los años que faltan para jubilarse son: {anios_faltantes}\n\
Los años con los cual se jubilaria son: {edad_jubilacion}')
