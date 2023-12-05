with open("input.txt", "r") as f:
  # Lese den Inhalt der Datei in eine Zeichenkette ein
  data = f.read()
header = data.split("seed-to-soil map:")
temp = header[0].split(":")
list_of_seeds = temp[1].split()
list_of_seeds.sort() #list_of_seeds ist das war wir brauchen list mit den seeds

temp2 = header[1].split("soil-to-fertilizer map:")
temp3 = temp2[1].split("fertilizer-to-water map:")
temp4 = temp3[1].split("water-to-light map:")
temp5 = temp4[1].split("light-to-temperature map:")
temp6 = temp5[1].split("temperature-to-humidity map:")
temp7 = temp6[1].split("humidity-to-location map:")

seed_to_soil = temp2[0]
soil_to_fertilizer = temp3[0]
fertilizer_to_water = temp4[0]
water_to_light = temp5[0]
light_to_temperature = temp6[0]
temperature_to_humiditiy = temp7[0]
humidity_to_temperature = temp7[1]

seed_to_soil_map = {}
soil_to_fertilizer_map = {}
fertilizer_to_water_map = {}
water_to_light_map = {}
light_to_temperature_map = {}
temperature_to_humiditiy_map = {}
humidity_to_temperature_map = {}

entries_seed_to_soil = seed_to_soil.split()

for i in range(len(entries_seed_to_soil)):
    destination = int(entries_seed_to_soil[i])
    source = int(entries_seed_to_soil[i+1])
    length = int(entries_seed_to_soil[i+1])
    i = i+2
    for i in range(length):
       seed_to_soil_map[destination+i] = source + i
   

# ex = humidity_to_temperature.split()
# list = []
# for entry in ex:
#   list.append(entry)
# print(humidity_to_temperature)
# print(list)