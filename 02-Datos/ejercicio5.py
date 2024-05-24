"""
    Create a program with a predefined list of people. Ask the user for his name, add it to the end of the list and print the update list.
"""

people = ["Cristel", "Alexandra"]

name = input("Ingrese su nombre: ")

people.append(name)

for data in people:
    print("User: " + data)