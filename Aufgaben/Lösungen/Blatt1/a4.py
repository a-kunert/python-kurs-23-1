counter = 0

for k in range(1, 1000001):
    if k % 100 == 99 and k % 7 == 0:
        counter += 1

print(f"Es gibt {counter} Zahlen, die diese Bedingung erfüllen")