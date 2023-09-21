from funciones import *
def main():
    mostrar_productos()
    medio_pago = elegir_medio_pago()
    menu_general(medio_pago)

# buena practica
if __name__ == "__main__":
    main()