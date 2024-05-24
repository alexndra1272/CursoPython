"""
    Create a program to calculate the area and circunference of a circle.
    Ask the user for the radius.
"""
from math import pi

# Validamos que sea una variable numerica
try:    
    radius = float(input("Ingrese el radio de la circunferencia: "))
    print(f"Area: {pi * (radius ** 2)}\nCircunferencia: {2 * pi * radius}")
except:
    print("ERROR: Ingrese un dato valido")