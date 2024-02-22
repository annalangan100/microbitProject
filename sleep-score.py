data = []

temp_data = [10,10,11,14,40,20,19,-100]
sound_data = [12,100,30,12,24,56,0,0,10]

for i in range(len(temp_data)):
    print(temp_data[i])
    
    if temp_data[i] > -10 and temp_data[i] < 30 :
        data.append(temp_data[i])
    else:
        print("Value:", temp_data[i], "is not a valid value")
        
for i in range(len(sound_data)):
    print(sound_data[i])
    
    if sound_data[i] > -10 and sound_data[i] < 50 :
        data.append(sound_data[i])
    else:
        print("Value:", sound_data[i], "is not a valid value")

        
print(data)