"""###**Ejercicio 3.19**
El programa debe:
*     Preguntar al usuario una cantidad de dinero a invertir
*     Preguntar al usuario el interés anual y el número de años
*     Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión."""
try:
    
    dinero = float(input('Ingrese el dinero a invertir: '))
    interes = float(input('Ingrese el interes (porcenate): '))
    num_anios = int(input('Ingrese los años: '))
    diner_acumulado = 0 
    for anio in range(0,num_anios):
        diner_acumulado = dinero + dinero*interes
        dinero = diner_acumulado
    #664
    print(f'El interes compuesto = {diner_acumulado}')
except Exception as e:
    print(e)