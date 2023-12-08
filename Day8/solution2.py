file = open("input.txt", "r")


sequence  = "LLRRRLLRLRRRLLRLRLRLRLRRRLRRLRRLRLLLRRLLRRLRRLRRLRRRLLLRRLRLRRRLRRRLRLRRLRRRLRLRRRLRLRLLLRLRRLRLRRLRRRLRLRRRLRRRLRRRLRRRLRLRRRLRRRLRLLRRLRLRLRRRLRRLRRRLRRRLRRRLRRRLLLLRRLLRLRRLRRLRRRLRRRLLLRRLRRLRLRRLRRRLRRLRLRRRLRLRRLLRLLRRLRLRRRLRRLRRLRLRRLLLRRRLRLRRRLRLRLLRLRLRRRLRLRLRRRLRRLRRLRRRLRRLLRRRR"
# for zeile in file:
#     counter += 1
#     if counter==2:
#         break
#     sequence=sequence+zeile
# print(sequence+"end")
# sequence.replace("\n","").replace(" ","")
# print(sequence + "end")


bitch = {}

counter = 0

for zeile in file:
        if counter>1:
            temp = zeile.split(" = ")
            tupel = temp[1].split(",")
            left = tupel[0].replace("(","")
            right = tupel[1].replace(")","").replace("\n","").replace(" ","")
            bitch[temp[0]] = (left,right)
        counter += 1




# def rekursiv(value, char, counter):
#     if(value == 'ZZZ'):
#         return counter
#     counter += 1
#     if(char == 'L'):
#         rekursiv(bitch[value][0],sequence[counter%len(sequence)], counter)
#     else:
#         rekursiv(bitch[value][1],sequence[counter%len(sequence)], counter)
# print(rekursiv('AAA','L',0))
    

counter3=0
counter_durchlauf = 0
def check_end(value):
    while(value.endswith('Z')):
        for char in sequence:
            # if counter3== 0:
            #      break
            if value.endswith('Z'):
                return true 
            if value == "":
                value = 'AAA'
            if char == 'L':
                value = bitch[value][0]
            else:
                value = bitch[value][1]
            counter_durchlauf += 1
        # counter3 = 1

while(True):
    if (check_end('GPA') and check_end('GTA') and check_end('VDA') and check_end('BBA') and check_end('AAA') and check_end('VSA')):
        print(counter_durchlauf)


print(counter_durchlauf)
list = []
for key in bitch:
    if key.endswith('A'):
        list.append(key)
print(list)

      


