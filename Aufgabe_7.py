# Aufgabe 7 - Break, Continue
def is_prime(p):
    prime = True
    for ind in range(2, p):
        if p % ind == 0:
            prime = False  # Nicht prim, wenn teilbar durch eine Zahl außer 1 und sich selbst
            break  # Schleife abbrechen
    return prime

n = int(input("Geben Sie die Obergrenze der Zahlen ein:\n"))
primeList = []
i = 2
while True:
    if is_prime(i):
        primeList.append(i)  # Primzahl zur Liste hinzufügen
    i += 1  # Nächste Zahl prüfen
    if i == n:
        break  # Schleife beenden, wenn Obergrenze erreicht
print("Die Liste der Primzahlen ist:", primeList)  # Liste der Primzahlen ausgeben