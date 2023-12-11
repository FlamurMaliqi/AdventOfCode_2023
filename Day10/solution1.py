data = open("input.txt", "r").read().splitlines()

def findStart(data):
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == "S":
                return (x,y)

start = findStart(data)

up,down,left,right = (-1,0),(1,0),(0,-1),(0,1)

tiles = {
    "S":[up,down,left,right],
    "|":[up,down],
    "-":[left,right],
    "L":[up,right],
    "J":[up,left],
    "7":[down,left],
    "F":[down,right],
    ".":[]
}
def loop(data,start,dir):
    acc = 0
    x,y = start
    visited = set()
    while acc == 0 or (x,y) != start:
        visited.add((x,y))
        dx,dy = dir
        x += dx
        y += dy
        if not (0<=x<len(data) and 0<=y<len(data[0])):
            return None
        dx *= -1
        dy *= -1
        tileDir = tiles[data[x][y]]
        if (dx,dy) not in tileDir:
            return None
        for nextDir in tileDir:
            if nextDir != (dx,dy):
                dir = nextDir
        acc += 1
    return acc, visited

goodResult = None
S = []
for dir in up,down,left,right:
    result = loop(data,start,dir)
    if result is not None:
        goodResult = result
        S.append(dir)

print(goodResult[0]//2)

visited = goodResult[1]
tiles["S"] = S

hand = None
acc = 0
for x in range(len(data)):
    inside = False
    for y in range(len(data[0])):
        if (x,y) in visited:
            tileDir = tiles[data[x][y]]
            if left in tileDir and right in tileDir:
                continue
            inside = not inside
            if up in tileDir and down in tileDir:
                continue
            tileHand = None
            for dir in tileDir:
                if dir != left and dir != right:
                    tileHand = dir
            if hand == None:
                hand = tileHand
            else:
                if tileHand != hand:
                    inside = not inside
                hand = None
        else:
            if inside:
                acc += 1
print(acc)