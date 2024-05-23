"""
    Create a program that ask the user for a number of kilometers, converts it to Miles and prints the result
    1 Mile = 1.609344Km
"""

# This function returns a float
def convertToMiles(kilometers :float):
    return kilometers / 1.6093440

km = float(input("Ingrese el numero de km: "))

print(convertToMiles(km))