first_name = input("Dein Vorname: ")
last_name = input("Dein Nachname: ")
street = input("Deine Straße: ")
house_number = input("Deine Hausnummer: ")
zip_code = input("Deine PLZ: ")
city = input("Deine Stadt: ")

# linefeeds can be created by using the special charakter \n
print(f"{first_name} {last_name}\n{street} {house_number}\n{zip_code} {city}")