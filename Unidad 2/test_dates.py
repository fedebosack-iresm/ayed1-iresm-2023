from datetime import date

# creating the date object of today's date
todays_date = date.today()
anio_actual = todays_date.year

edad = int(input("Ingrese su edad: "))
print(f"Su edad es {edad} años")
calculado = anio_actual-edad
print(f'Usted nacio en el año {calculado}/{calculado-1}')