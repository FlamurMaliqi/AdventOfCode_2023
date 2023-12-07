from collections import Counter

file = open("input.txt", "r")

hand=[]
bid=[]

map = {}


def häufigstes_zeichen(s):
    c = Counter(s)
    
    häufigstes = c.most_common(1)
    
    return häufigstes[0] 

for zeile in file:
    temp = häufigstes_zeichen(zeile.split()[0])
    temp2 = (zeile.split()[0],zeile.split()[1])
    map[temp2] = temp

länge = len(map)
for i in range(länge-1):
    for j in range(länge-1):
        if(map[])



