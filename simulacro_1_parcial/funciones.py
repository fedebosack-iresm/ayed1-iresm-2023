'''
1. Permitir al usuario del programa agregar un nuevo videojuego (Indicando: Nombre - Año - Categoria)
       Verificando: Que el nombre no exista previamente, el año este entre 1990 y 2021 y que la categoria corresponda
       con una lista de categorias.(Ayuda: metodo in de list)
       IMPORTANTE: se debe crear una matriz para contener los datos, listas dentro de listas.
'''
lista_categorias = ["Acción", "Deportivo", "Estrategia", "Simulación"]
video_juegos=[[],[],[]]
def agregar_video_juego():
    while True:
        nombre = input('Ingrese el nombre del videojuego: ')
        if nombre in video_juegos[0]:
            print('El nombre ya existe')
        else:
            break
    
    while True:
        try:
            anio = int(input('Ingrese el año del videojuego: '))
            if 1990 < anio < 2021:
                break
            else:
                print('el año debe estar entre 1990 y 2021')
        except Exception as e:
            print('Ingrese un numero entero!')

    while True:
        categoria = input('Ingrese la categoria del videojuego: ')
        if categoria not in lista_categorias:
            print(f'La categoria debe ser: {lista_categorias}')
        else:
            break
    
    video_juegos[0].append(nombre)
    video_juegos[1].append(anio)
    video_juegos[2].append(categoria)

'''2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)'''

def ver_video_juegos():
    print('-- nombre -- año -- categoria')
    for i in range(len(video_juegos[0])):
        print(f'{video_juegos[0][i]}-{video_juegos[1][i]}-{video_juegos[2][i]}')

'''3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.'''

def modificar_categoria():
    while True:
        nombre = input('Ingrese el nombre del videojuego a modificarle la categoria: ')
        if nombre in video_juegos[0]:
            break
        else:
            print(f'el video juego {nombre} no existe')
    
    while True:
        categoria = input('Ingrese la categoria del videojuego: ')
        if categoria not in lista_categorias:
            print(f'La categoria debe ser: {lista_categorias}')
        else:
            break
    index = video_juegos[0].index(nombre)
    video_juegos[2][index] = categoria
    
'''4. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).'''
def agregar_categoria():
    while True:
        categoria = input('Ingrese la nueva categoria del videojuego: ').capitalize()
        if categoria not in lista_categorias:
            lista_categorias.append(categoria)
            print(lista_categorias)
            break
        else:
            print('la categoria no puede ser repetida')

'''5. Eliminar una categoria del sistema, verificando previamente su existencia'''
def eliminar_categoria():
    while True:
        categoria = input('Ingrese la categoria del videojuego a eliminar: ').capitalize()
        if categoria in lista_categorias:
            lista_categorias.remove(categoria)
            print(lista_categorias)
            break
        else:
            print(f'la categoria {categoria} no esta en el sistema')
