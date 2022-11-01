# Part (a)
length = input("Länge in Meter: ")
length = float(length)
print(f"Die Länge in Kilometern beträgt {length/1000}km")

# Part (b)
temp = input("Temperatur in Grad Celsius: ")
temp = float(temp)
temp = temp + 273.15
temp = int(temp * 100)/100  # my creative way to round to 2 figures
print(f"Die Temperatur in Grad Kelvin beträgt {temp}")

# Part (c)
length = input("Länge in Zentimeter: ")
length = float(length)
length = length/2.54
length = int(length*100)/100  # my creative way to round to 2 figures
print(f"Die Länge in Zoll beträgt {length}")

# Part (d)
temp = input("Temperatur in Grad Celsius: ")
temp = float(temp)
temp = 9/5 * temp + 32  # you find this conversion rule on Wikipedia
temp = int(temp * 100)/100  # my creative way to round to 2 figures
print(f"Die Temperatur in Grad Fahrenheit beträgt {temp}")


