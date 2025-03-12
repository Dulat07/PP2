def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

grams = float(input("Enter the amount in grams: "))
ounces = grams_to_ounces(grams)
print(f"{grams} grams is equal to {ounces:.2f} ounces.")