try:
    num1 = int(input('ingrese un numero'))
    num2 = int(input('ingrese numero limite'))
    while (num1 <= num2):
        print (f'repeticion {num1}')
        num1+=1
    print ('estoy fuera del while')
except Exception as e:
    print(e)