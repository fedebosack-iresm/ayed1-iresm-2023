
base_taxis = [["IRM-200","ABC-123","LOI-555"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int

def pedir_un_str(texto_para_pedir):
    while True:
        variable_str = input(texto_para_pedir)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()

'''3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60'''

def cambiar_recorrido_auto(base_taxis):
    while True:
        patente = pedir_un_str('Dame la patente del auto a cambiar el chofer: ')
        if patente in base_taxis[0]:
            nuevo_recorrido = pedir_un_int('Dame el nuevo recorrido: ')
            index = base_taxis[0].index(patente)
            base_taxis[2][index] = nuevo_recorrido
            return base_taxis
        else:
            print('No existe esa patente!')

def cambiar_chofer_auto(base_taxis):
    while True:
        patente = pedir_un_str('Dame la patente del auto a cambiar el chofer: ')
        if patente in base_taxis[0]:
            nuevo_nombre = pedir_un_str('Dame el nombre del nuevo chofer: ')
            index = base_taxis[0].index(patente)
            base_taxis[1][index] = nuevo_nombre
            return base_taxis
        else:
            print('No existe esa patente!')

def imprimir_recorrdidos(base_taxis):
    recorrido = pedir_un_int('Ingrese el recorrido del viaje: ')
    print('Posibles choferes')
    for i in range(len(base_taxis[2])):
        if recorrido <= base_taxis[2][i]:
            print(f'auto: {base_taxis[0][i]} - chofer: {base_taxis[1][i]}')