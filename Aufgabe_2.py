# Aufgabe 2 - While True
boolean = True
i = 0
while boolean:
    print(i)  # Aktuellen Wert von i ausgeben
    i += 1  # i um 1 erhöhen
    if i == 50000:
        boolean = False  # Schleife beenden, wenn i 50000 erreicht