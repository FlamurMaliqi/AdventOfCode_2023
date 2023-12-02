file = open("input.txt", "r")


def SemicolonId(zeile):
    for char in zeile:
        if char == ';':
            return True
    return False


def getSemicolonID(zeile):
    counter = 0
    for char in zeile:
        if char == ':':
            return counter
        counter = counter + 1


def getID(zeile):
    counter = 0
    for char in zeile:
        if char == ':':
            return counter - 1
        counter = counter + 1


def checkIfPass(zeile):
    green = 0
    blue = 0
    red = 0
    for i in range(len(zeile) - 1):
        if zeile[i].isdigit():
            count = int(zeile[i])
            if zeile[i + 2] == 'g':
                green += count
            elif zeile[i + 2] == 'r':
                red += count
            elif zeile[i + 2] == 'b':
                blue += count
    return red <= 12 and blue <= 14 and green <= 13


for zeile in file:
    summe = 0
    id = getID(zeile)
    valueOfId = int(zeile[id])
    while SemicolonId(zeile):
        semicolon = getSemicolonID(zeile)
        if semicolon is None:
            break  # Beende die Schleife, wenn kein Semikolon gefunden wird
        subset = zeile[id:semicolon]
        if checkIfPass(subset):
            summe = summe + 0
        else:
            summe = summe + valueOfId
        zeile = zeile[semicolon + 1:]


print(summe)
