base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }

def listar_series_y_peliculas(base: dict):
    print('----Peliculas-----')
    for i in base["peliculas"]:
        print(i)
    print('----Series-----')
    for i in base["series"]:
        print(i)

def eliminar_serie(base: dict):
    serie_a_eliminar = input('Ingrese la serie a eliminar: ')
    if serie_a_eliminar in base["series"]:
        indice = base["series"].index(serie_a_eliminar)
        base["series"].pop(indice)
        
    else:
        print('No existe la serie')
    return base

eliminar_serie(base)
listar_series_y_peliculas(base)
