# Aufgabe 10 - Matrix-Generator
rows = int(input("Geben Sie die Anzahl der Zeilen ein:\n"))
columns = int(input("Geben Sie die Anzahl der Spalten ein:\n"))
myMatrix = [[0 for col in range(columns)] for row in range(rows)]  # Matrix mit Nullen erstellen
for i in range(len(myMatrix)):
    print(myMatrix[i])  # Jede Zeile der Matrix ausgeben