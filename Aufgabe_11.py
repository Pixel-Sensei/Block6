# Aufgabe 11 - Gültiges Passwort
import string
password = input("Geben Sie ein neues Passwort ein:\n")
length = False
spec_char = False
letter_char = False
digit_char = False
low = False
cap = False
for i in password:
    if i.isalpha():
        letter_char = True  # Es gibt Buchstaben
    if i.isdigit():
        digit_char = True  # Es gibt Ziffern
    if i.islower():
        low = True  # Es gibt Kleinbuchstaben
    if i.isupper():
        cap = True  # Es gibt Großbuchstaben
    if i in string.punctuation:
        spec_char = True  # Es gibt Sonderzeichen
    if 6 <= len(password) <= 16:
        length = True  # Passwortlänge ist korrekt
if length and spec_char and cap and low and digit_char and letter_char:
    print("Dies ist ein gültiges Passwort")  # Passwort ist gültig
else:
    print("Dies ist kein gutes Passwort")  # Passwort ist ungültig