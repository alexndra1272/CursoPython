"""
    Create a program that ask the user for this birthday in the 
    format "DD-MM-YYYY". Then print:
    You were born in [month]
"""

months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

birthday = input("Ingresa tu cumple (DD-MM-YYYY): ")
month = int(birthday.split("-")[1]) - 1

try:
    print(f"Naciste en {months[month]}")
except:
    print("La fecha que ingresaste no es valida")