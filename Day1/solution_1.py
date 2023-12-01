# Datei öffnen
file = open("input.txt", "r")

firstNumber = 0
lastNumber = 0
summe = 0
zahlinZeile = 0
for zeile in file:
    for char in zeile:
        if(char.isdigit()):
            if(firstNumber == 0):
                firstNumber = int(char)
            lastNumber = int(char)
    zahlinZeile = firstNumber*10 + lastNumber
    summe = summe + zahlinZeile
    
    firstNumber = 0
    lastNumber = 0
print(summe)
file.close()
