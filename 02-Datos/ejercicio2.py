"""
    Let's say your company has a product with this lot number: "037-009001-00027".
    037 is the country code. 00901 is the product code. 00027 is the batch number.
    Create a program to print:
    Country code: ___
    Product code: _____
    Batch number: _____
"""

lotNumber = input("Lot number: ")

if len(lotNumber) != 16:
    exit()

data = lotNumber.split("-")

print(f"Country code: {data[0]}\nProduct code: {data[1]}\nBatch number: {data[2]}")