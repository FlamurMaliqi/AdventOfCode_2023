# Datei öffnen
file = open("input.txt", "r")

def replace_text_numbers(input_string):
    number_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for word, number in number_mapping.items():
        input_string = input_string.replace(word, number)

    return input_string

firstNumber = 0
lastNumber = 0
summe = 0
zahlinZeile = 0

for zeile in file:
    zeile1 = replace_text_numbers(zeile)
    for char in zeile1:
        if(char.isdigit()):
            if(firstNumber == 0):
                firstNumber = int(char)
            lastNumber = int(char)
    zahlinZeile = firstNumber * 10 + lastNumber
    summe = summe + zahlinZeile

    firstNumber = 0
    lastNumber = 0

print(summe)
file.close()
