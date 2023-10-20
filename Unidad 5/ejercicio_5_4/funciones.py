def pedir_un_str(texto_para_pedir):
    while True:
        variable_str= input(texto_para_pedir)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()