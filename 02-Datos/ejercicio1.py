"""
    Create a program that ask the user for his first name, his middle name
    and his last name. Then print: Your initials are ___
"""


# Solicitamos el primer nombre
firstName = input("Ingrese su primer nombre: ")
middleName = input("Ingrese su segundo nombre: ")
lastName = input("Ingrese su apellido: ")

# Salida
print(f"Sus iniciales son {firstName[0].upper()}{middleName[0].upper()}{lastName[0].upper()}")