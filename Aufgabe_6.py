# Task 6 - Letters in string
myString = input("Input a string\n")
digits = 0
letters = 0
for char in myString:
    if char.isdigit():
        digits = digits + 1
    elif char.isalpha():
        letters = letters + 1
    else:
        pass
print("Letters:", letters)
print("Digits:", digits)