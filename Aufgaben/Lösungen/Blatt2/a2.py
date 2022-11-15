# Man verwendet statt ganzen Euros lieber Cents
# Der Unterstrich innerhalb einer Zahl dient nur zur Übersichtlichkeit
# und kann ignoriert werden (z.B. 50_00 = 5000)

# Teil A
value = 3000_00
interest = 0.0028
rate = 50_00

for month in range(1, 12 * 15 + 1):
    value += rate
    value += interest * value
    value = round(value)
print(f"a) In Monat {month} beträgt der Wert {value/100}€")

# Teil B
month = 0
value = 3000_00

while interest * value < rate:
    month += 1
    value += rate
    value += interest * value
    value = round(value)

print(f"b) Nach {month} Monaten gibt der Zinssatz mehr als die Sparrate")

# Teil C
value = 3000_00
alt_value = 3000_00
alt_rate = 10_00
alt_interest = 0.009
month = 0

while alt_value <= value:
    month += 1
    value += rate
    value += interest * value
    value = round(value)
    alt_value += alt_rate
    alt_value += alt_interest * alt_value
    alt_value = round(alt_value)

print(f"c) Nach {month} Monaten ist das zweite Modell besser")

value = 3000_00
alt_value = 3000_00

for month in range(1, 12 * 20 + 1):
    value += rate
    value += interest * value
    value = round(value)
    alt_value += alt_rate
    alt_value += alt_interest * alt_value
    alt_value = round(alt_value)

print(f"d) Nach 20 Jahren beträgt die Differenz gleich {alt_value/100} - {value/100} = {(alt_value - value)/100}")