
time = 41777096
distance = 249136211271011
variance = 0

for j in range(time): #j ist gedrückt
    speed = j*1
    restTime = time - j
    distanceReached = speed * restTime
    if (distanceReached > distance):
        variance += 1

print(variance)
