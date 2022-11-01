counter = 1
n = 1000000000

while n != 1:
    counter += 1
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n + 1

print(f"Die Folge ist nach {counter} Folgengliedern zu Ende")