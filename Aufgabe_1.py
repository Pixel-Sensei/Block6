# Aufgabe 1 - Modulo 3
myNum = int(input("Geben Sie eine ganze Zahl ein:\n"))
while myNum > 1:
    # Überprüfen, ob die Zahl durch 3 teilbar ist
    if myNum % 3 == 0:
        myNum /= 3  # Wenn ja, die Zahl durch 3 teilen
    else:
        myNum += 1  # Wenn nein, 1 zur Zahl hinzufügen
    print(myNum)  # Aktuellen Wert der Zahl ausgeben
print(myNum)  # Endwert der Zahl ausgeben