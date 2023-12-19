with open("input.txt", "r") as f:
  # Lese den Inhalt der Datei in eine Zeichenkette ein
  data = f.read()
string = data.split(",")
sum = 0
temp = 0
for entry in string:
    for char in entry:
        temp += ord(char)
        temp = temp*17
        temp = temp%256
    sum += temp
    temo = 0

print(sum)