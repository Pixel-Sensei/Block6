# Aufgabe 9 - Zahl umkehren
num = int(input("Geben Sie eine ganze Zahl ein:\n"))
reverse_number = 0
print("Gegebene Zahl ", num)
while num > 0:
    reminder = num % 10  # Letzte Ziffer der Zahl erhalten
    reverse_number = (reverse_number * 10) + reminder  # Letzte Ziffer zur umgekehrten Zahl hinzufügen
    num = num // 10  # Letzte Ziffer von der Zahl entfernen
print("Umgekehrte Zahl ", reverse_number)  # Umgekehrte Zahl ausgeben