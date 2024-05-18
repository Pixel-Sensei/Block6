# Aufgabe 8 - Schleife-else
basket = {'Apfel': 20, 'Banane': 30, 'Orange': 10}
fruit = input('Geben Sie eine Frucht ein:')
index = 0
for item in basket:
    if item == fruit:
        print("Der Korb hat ", basket[item], " ", item, ".", sep="")
        break  # Schleife beenden, wenn Frucht gefunden
else:
    quantity = int(input(f"Geben Sie die Menge von {fruit} ein:\n"))
    basket[fruit] = quantity  # Neue Frucht und Menge zum Korb hinzufügen
    for item in basket:
        print(item, ": ", basket[item], sep="")  # Alle Früchte im Korb ausgeben