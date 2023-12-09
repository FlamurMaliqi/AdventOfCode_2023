file = open("input.txt", "r")


def distance(numbers):
    for i in range(len(numbers)-1):  
        if numbers[i] - numbers[i+1] != 0:  
            return False
    return True


def solve(numbers):
    numbers_distance = []
    if(distance(numbers)):
        return True
    else:
        for i in range(len(numbers-2)):
            numbers_distance.append(numbers[i]- numbers[i+1])
        return solve(numbers_distance)

for zeile in file:
    zahlen = zeile.split()
    while(solve(zahlen)):
        