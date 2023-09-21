"""
###**Ejercicio 2.4:**
El programa debe:
*  pedir por teclado el dinero actual de una persona
*  pedir por teclado el precio del insumo que quiere comprar en USD
*  convertir ese dinero a dolares( 1USD -> 730$)
*  devoler por pantalla True en caso que pueda comprar, False en caso que no
*  No deben aparecer errores
"""
precio_dolar = 730
dinero = float(input("Indique su dinero actual (en pesos AR): "))
insumo = float(input("Indique el precio del insumo (en USD): ")) * precio_dolar
print(f"con {dinero}$AR puedo comprar el insumo de {insumo}? {dinero>=insumo}")