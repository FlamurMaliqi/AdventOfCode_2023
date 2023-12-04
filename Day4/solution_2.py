file = open("input.txt", "r")

list_winning_numbers = []
list_numbers_you_have = []
zahl = 0
summe = 0
with open("input.txt", "r") as datei:
    lines = datei.readlines()

dictionary = {}
dictionary[1] = 1
index = 1
for zeile in file:
    saetze = zeile.split('|')
    winning_numbers = saetze[0].split(':')
    for char in winning_numbers[1]:
        if(char.isdigit()):
            zahl = zahl*10 + int(char)
            continue
        if (zahl != 0):
            list_winning_numbers.append(zahl)
        zahl = 0
    for char in saetze[1]:
        if(char.isdigit()):
            zahl = zahl*10 + int(char)
            continue
        if (zahl != 0):
            list_numbers_you_have.append(zahl)
        zahl = 0
    list_numbers_you_have.sort()
    list_winning_numbers.sort()
    counter = 0
    copy = dictionary[index]

    for i in range(copy):
        for unit in list_winning_numbers:
            for unit2 in list_numbers_you_have:
                if unit2 == unit:
                    counter = counter + 1
    
    for i in range(counter):
        dictionary[index+i+1] += 1*copy
    list_numbers_you_have = []
    list_winning_numbers = []
    index = index + 1 
    anzahl_der_karten = 0
    for value in dictionary:
        anzahl_der_karten = anzahl_der_karten + value

print(anzahl_der_karten)

        