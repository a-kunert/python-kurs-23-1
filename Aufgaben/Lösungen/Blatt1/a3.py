x = input("Gib die 1. Zahl ein: ")
y = input("Gib die 2. Zahl ein: ")
z = input("Gib die 3. Zahl ein: ")

x = int(x)
y = int(y)
z = int(z)


if x >= y:
    if z >= x:
        result = z
    else:
        result = x
else:
    if z >= y:
        result = z
    else:
        result = y

print(f"Die größte der drei Zahlen ist {result}")