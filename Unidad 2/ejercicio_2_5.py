"""
##**Ejercicio 2.5**
El programa debe:
- pedir dos datos por consola
- verificar que los dos datos sean numeros enteros
- en caso verdadero imprimir la suma de ambos
- en caso contrario imprimir error
"""
#num_1 = 0
#num_2 = 0
try:
    num_1 = int(input("Dame un numero: "))
    num_2 = int(input("Dame otro numero: "))
    print(f"la suma de ambos numeros es: {num_1+num_2}")
except Exception as e:
    print(f"error: {e}")

