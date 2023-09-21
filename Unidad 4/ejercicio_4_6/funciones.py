producto_1_nombre = 'producto_1'
producto_2_nombre = 'producto_2'
producto_3_nombre = 'producto_3'

producto_1_precio = 300
producto_2_precio = 400
producto_3_precio = 500

producto_1_stock = 5
producto_2_stock = 4
producto_3_stock = 7

#medio_pago = ''

def mostrar_productos():
    print(f'nombre \t\t precio \t stock')
    print(f'{producto_1_nombre} \t {producto_1_precio} \t\t {producto_1_stock}')
    print(f'{producto_2_nombre} \t {producto_2_precio} \t\t {producto_2_stock}')
    print(f'{producto_3_nombre} \t {producto_3_precio} \t\t {producto_3_stock}')

def elegir_medio_pago():
    while True:
        opcion_1 = input('''
Eliga el medio de pago
- Efectivo (E)
- Tarjeta debito (TD))
- Tarjeta credito (TC))
Opcion: ''')
        if opcion_1.lower() == 'e':
            return 'e'
        elif opcion_1.lower() == 'td':
            return 'td'
        elif opcion_1.lower() == 'tc':
            return 'tc'
        else:
            print('opcion incorrecta')

def comprar_producto(medio_pago):
    producto_comprar = input('eliga el producto a comprar: ')
    # verificar si el producto es un producto con las variables
    pass

def menu_general(medio_pago):
    while True:
        opcion = input('''
Eliga una opcion
  1. Ver menu de productos
  2. Comprar un producto
    -  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock)
    -  Pagar con tarjeta debito (se debe descontar el stock)
    -  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
  3.  consultar productos y stock
  4.  agregar stock a los productos
  5.  cambiar el precio a los productos
  6.  Salir
Opcion: ''')
        if opcion == '1':
            comprar_producto(medio_pago)
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        else:
            print('opcion incorrecta')
