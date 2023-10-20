#from funciones import pedir_un_str
import funciones
def main():
    lista=[]
    
    for i in range (0,5):
        materia = funciones.pedir_un_str(f'ingrese {i+1} materia: ')
        lista.append(materia)
    
    lista.sort()
    print(f'las materias ordenadas alfabeticamente son las siguiente: {lista}')


if __name__ == "__main__":
    main()