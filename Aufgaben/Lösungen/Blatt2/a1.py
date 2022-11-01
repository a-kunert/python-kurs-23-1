value = 3000
interest = 0.0028
rate = 50

for month in range(1, 12 * 15 + 1):
    value += rate
    value += interest * value
    value = round(value)

print(f"In Monat {month} beträgt der Wert {value}€")
month = 0


value = 3000

while interest * value < rate:
    month += 1
    value += rate
    value += interest * value
    value = round(value)

print(f"Nach {month} Monaten gibt der Zinssatz mehr")


value = 3000
alt_value = 3000
alt_rate = 10
alt_interest = 0.009

for month in range(1, 12 * 15 + 1):
    alt_value += alt_rate
    alt_value += alt_interest * alt_value
    alt_value = round(alt_value)
print(f"In Monat {month} beträgt der Wert {alt_value}€")

value = 3000
alt_value = 3000
month = 0
while alt_value <= value:
    month += 1
    value += rate
    value += interest * value
    value = round(value)
    alt_value += alt_rate
    alt_value += alt_interest * alt_value
    alt_value = round(alt_value)

print(f"Nach {month} Monaten ist das zweite Modell besser")


value = 3000
alt_value = 3000

for month in range(1, 12 * 20 + 1):
    value += rate
    value += interest * value
    value = round(value)
    alt_value += alt_rate
    alt_value += alt_interest * alt_value
    alt_value = round(alt_value)

print(f"In Monat {month} beträgt der Wert {value}€")
print(f"Alt: In Monat {month} beträgt der Wert {alt_value}€")
month = 0
