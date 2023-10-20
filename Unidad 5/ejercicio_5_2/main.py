def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int

def main():
    lista = []
    cant_personas = pedir_un_int('Ingrese la cant de personas: ')
    for i in range(0,cant_personas):
        edad = pedir_un_int(f'Ingrese la edad de la persona {i+1}: ')
        lista.append(edad)
    lista.sort()
    print(f'La mayor edad en la lista es: {lista[-1]}')

if __name__ == "__main__":
    main()
