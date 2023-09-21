"""
### **Ejercicio 3.6:**
*  Pedir a un usuario la temperatura (castear)
*  Determinar si con esa temperatura una persona tiene fiebre, esta congelado o sano. 
  - fiebre : 37.5 y 40 grados)
  - si esta congelado (menor de 20°)
  - sino esta sano
  
IMPORTANTE!: No tienen que aparecer errores!"""
temp = None
try:
    temp = float(input('Ingrese la temperatura: '))
except Exception as e:
    print(f'Error {e}')

if(temp == None):
     print('temp incorrecta')
elif(temp >=37.5 and temp <40):
        print('Usted tiene fiebre!!!')
elif(temp < 20):
    print('Estas congelado!!')
elif(temp > 40):
    print('Mucho calor!!')
else:
    print('Usted esta sano')