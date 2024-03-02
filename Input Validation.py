data = []

temp_data =  [28, 28, 27, 27, 27, 27, 26, 26, 26, 13, 26, 14, 26, 26, 26, 26, 26, 26, 25, 26, 15, 25, 12, 13, 25, 25, 25, 14, 25, 25]
sound_data = [0, 7, 26, 0, 0, 15, 0, 3, 33, 7, 3, 0, 0, 7, 0, 0, 7, 3, 3, 0, 3, 3, 15, 3, 3, 3, 7, 3, 0, 0]
light_data = [190, 0, 0, 0, 184, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 181, 3, 3, 2, 2, 2, 35, 2, 2, 2, 189, 5, 5, 6]


for i in range(len(temp_data)):
    print(temp_data[i])
    
    if temp_data[i] > -10 and temp_data[i] < 50:
        data.append(temp_data[i])
    else:
        print("Value: ", temp_data[i], "is not a valid value")
  
for i in range(len(light_data)):
    print(light_data[i])
    if light_data[i] > -10 and light_data[i] < 200:
        data.append(light_data[i])
    else:
        print("Value: ", light_data[i], "is not a valid value")

for i in range(len(sound_data)):
    print(sound_data[i])
    if sound_data[i] > -10 and sound_data[i] < 200:
        data.append(sound_data[i])
    else:
        print("Value: ", sound_data[i], "is not a valid value")
        
print(data)