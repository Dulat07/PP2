def fahrenheit_to_centigrade(f):
    
    c = (5 / 9) * (f - 32)
    return c

f = float(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_centigrade(f)
print(f"{f} Fahrenheit is equal to {c:.2f} Centigrade.")