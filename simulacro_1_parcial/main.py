from funciones import *

def main():
    while True:
        menu = """-->    Programa de Videojuego  <--

    1. Agregar un nuevo videojuego
    2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)
    3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.
    4. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).
    5. Eliminar una categoria del sistema, verificando previamente su existencia
    6. Salir
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == "1"):
            agregar_video_juego()
        elif(opcion == "2"):
            ver_video_juegos()
        elif(opcion == "3"):
            modificar_categoria()
        elif(opcion == "4"):
            agregar_categoria()
        elif(opcion == "5"):
            eliminar_categoria()
        elif(opcion == "6"):
            return
        else:
            print('Opcion incorrecta')

if __name__ == "__main__":
    main()