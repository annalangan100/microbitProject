import csv

temp_data =  [13, 28, 14, 27, 27, 27, 26, 26, 26, 13, 26, 14, 26, 26, 26, 26, 26, 26, 25, 26, 15, 25, 12, 13, 25, 25, 25, 14, 25, 25]
sound_data = [0, 7, 26, 0, 0, 15, 0, 3, 33, 7, 3, 0, 0, 7, 0, 0, 7, 3, 3, 0, 3, 3, 15, 3, 3, 3, 7, 3, 0, 0]
light_data = [190, 0, 184, 0, 0, 2, 0, 2, 2, 190, 2, 181, 2, 2, 2, 2, 181, 3, 3, 2, 186, 0, 190, 2, 2, 2, 189, 170, 5, 6]

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
    
    
import csv

day_data = [
    [1, 13, 0, 190],
    [2, 28, 7, 0],
    [3, 14, 26, 184],
    [4, 27, 0, 0],
    [5, 27, 0, 0],
    [6, 27, 15, 2],
    [7, 26, 0, 0],
    [8, 26, 3, 2],
    [9, 26, 33, 2],
    [10, 13, 7, 190],
    [11, 26, 3, 2],
    [12, 14, 0, 181],
    [13, 26, 0, 2],
    [14, 26, 7, 2],
    [15, 26, 0, 2],
    [16, 26, 0, 2],
    [17, 26, 7, 181],
    [18, 26, 3, 3],
    [19, 25, 3, 3],
    [20, 26, 0, 2],
    [21, 14, 3, 186],
    [22, 25, 3, 0],
    [23, 12, 15, 190],
    [24, 13, 3, 2],
    [25, 25, 3, 2],
    [26, 25, 3, 2],
    [27, 25, 7, 189],
    [28, 14, 3, 170],
    [29, 25, 0, 5],
    [30, 25, 0, 6]
]

# Write data to CSV file
with open("sleepscore.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Temperature", "Sound", "Light"])
    writer.writerows(day_data)

print("Data has been written to sleepscore.csv.")

import csv

def calculate_sleep_score(temperature, sound_level, light_level):
    score = 0

    # Check temperature conditions
    if 15 <= temperature <= 20:
        score += 33.333333333  # Increase sleep score by 33.333333333%
    
    # Check light level conditions
    if light_level < 180:
        score += 33.333333333  # Increase sleep score by 33.333333333%
    
    # Check sound level conditions
    if sound_level < 30:
        score += 33.333333333  # Increase sleep score by 33.333333333%
    
    return min(score, 100)  # Cap the sleep score at 100%

def get_sleep_data(day):
    # Load sleep data from CSV file
    with open('sleepscore.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['Day']) == day:
                return float(row['Temperature']), float(row['Sound']), float(row['Light'])
    return None

def get_sleep_advice(temperature, sound_level, light_level):
    advice = []

    # Temperature advice
    if temperature < 15:
        advice.append("Increase the room temperature to improve sleep.")
    elif temperature > 20:
        advice.append("Lower the room temperature to improve sleep.")

    # Light advice
    if light_level > 180:
        advice.append("Dim the lights or use blackout curtains to reduce light exposure.")

    # Sound advice
    if sound_level > 30:
        advice.append("Reduce noise levels by using earplugs or white noise machines.")

    return advice

# Ask user for the day number they want to check
day = int(input("Enter the day number you want to check (1 to 30): "))

if 1 <= day <= 30:
    # Get sleep data for the specified day
    sleep_data = get_sleep_data(day)

    if sleep_data:
        temperature, sound_level, light_level = sleep_data

        # Calculate sleep score as a percentage
        sleep_score_percentage = calculate_sleep_score(temperature, sound_level, light_level)

        print("Sleep Score Percentage for Day", day, ":", sleep_score_percentage, "%")

        # Get sleep advice
        advice = get_sleep_advice(temperature, sound_level, light_level)
        if advice:
            print("To improve your sleep:")
            for tip in advice:
                print("-", tip)
        else:
            print("No specific advice for improving sleep based on the data.")
    else:
        print("No data found for day", day)
else:
    print("Invalid day number. Please enter a number between 1 and 30.")


import csv

day_data = [
    [1, 13, 0, 190, 5],
    [2, 28, 7, 0, 6],
    [3, 14, 26, 184, 5],
    [4, 27, 0, 0, 7],
    [5, 27, 0, 0, 7],
    [6, 27, 15, 2, 6],
    [7, 26, 0, 0, 7],
    [8, 26, 3, 2, 7],
    [9, 26, 33, 2, 5],
    [10, 13, 7, 190, 4],
    [11, 26, 3, 2, 6],
    [12, 14, 0, 181, 5],
    [13, 26, 0, 2, 7],
    [14, 26, 7, 2, 6],
    [15, 26, 0, 2, 6],
    [16, 26, 0, 2, 7],
    [17, 26, 7, 181, 5],
    [18, 26, 3, 3, 7                                                                       ],
    [19, 25, 3, 3, 6],
    [20, 26, 0, 2, 6],
    [21, 14, 3, 186, 4],
    [22, 25, 3, 0, 7],
    [23, 12, 15, 190, 4],
    [24, 13, 3, 2, 5],
    [25, 25, 3, 2, 7],
    [26, 25, 3, 2, 7],
    [27, 25, 7, 189, 4],
    [28, 14, 3, 170,4],
    [29, 25, 0, 5, 6],
    [30, 25, 0, 6, 6]
]

# Write data to CSV file
with open("sleepscore.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Temperature", "Sound", "Light", "Sleep Time"])
    writer.writerows(day_data)

print("Data has been written to sleepscore.csv.")

