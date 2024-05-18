# Aufgabe 5 - Buchstaben in Zeichenkette
myString = input("Geben Sie eine Zeichenkette ein:\n")
digits = 0
letters = 0
for char in myString:
    if char.isdigit():
        digits += 1  # Zähler für Ziffern erhöhen
    elif char.isalpha():
        letters += 1  # Zähler für Buchstaben erhöhen
    else:
        pass  # Nichts tun bei anderen Zeichen
print("Buchstaben:", letters)  # Anzahl der Buchstaben ausgeben
print("Ziffern:", digits)  # Anzahl der Ziffern ausgeben