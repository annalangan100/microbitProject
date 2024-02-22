data = []

temp_data =  [28, 28, 27, 27, 27, 27, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 25, 26, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
sound_data = [0, 7, 26, 0, 0, 0, 0, 3, 33, 7, 3, 0, 0, 7, 0, 0, 7, 3, 3, 0, 3, 3, 15, 3, 3, 3, 7, 3, 0, 0]
light_data = [0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2, 35, 2, 2, 2, 5, 5, 5, 6]


for i in range(len(temp_data)):
    print(temp_data[i])
    
    if temp_data[i] > -10 and temp_data[i] < 30:
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

import csv

max_length = max(len(temp_data), len(sound_data), len(light_data))
temp_data += [None] * (max_length - len(temp_data))
sound_data += [None] * (max_length - len(sound_data))
light_data += [None] * (max_length - len(light_data))

file = open("sleepscore.csv", "w", newline="")
db = csv.writer(file)
db.writerow(["Temperature", "Sound", "Light"])  
for temp, sound, light in zip(temp_data, sound_data, light_data):
    db.writerow([temp, sound, light])
file.close()

file = open("sleepscore.csv", "r")
data_base = list(csv.reader(file))
file.close()

print("Temperature \t Sound \t\t Light")
print("---------------------------------------")
for data in data_base[1:]:  
    print("\t\t".join(data))

def calculate_sleep_score(temperature, light_level, sound_level):
    # Initialize sleep score increase to 0
    score_increase = 0

    # Check temperature conditions
    if 15 <= temperature <= 20:
        score_increase += 33.333333333  # Increase sleep score by 33.333333333%
    
    # Check light level conditions
    if light_level < 180:
        score_increase += 33.333333333  # Increase sleep score by 33.333333333%
    
    # Check sound level conditions
    if sound_level < 30:
        score_increase += 33.333333333  # Increase sleep score by 33.333333333%
    
    return score_increase

def calculate_sleep_score_percentage(score_increase):
    # Cap the sleep score increase at 100%
    return min(score_increase, 100)

# Example data
temperature = 28  # Degrees Celsius
light_level = 0  # Lux
sound_level = 7  # dB

# Calculate sleep score increase
score_increase = calculate_sleep_score(temperature, light_level, sound_level)

# Calculate sleep score as a percentage
sleep_score_percentage = calculate_sleep_score_percentage(score_increase)

print("Sleep Score Increase:", score_increase, "%")
print("Sleep Score Percentage:", sleep_score_percentage, "%")