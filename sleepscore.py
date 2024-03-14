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

csv_data = []
with open("sleepscore.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        csv_data.append([int(cell) for cell in row])

# Perform testing
if day_data == csv_data:
    print("Testing passed: Data written to CSV matches the original data.")
else:
    print("Testing failed: Data written to CSV does not match the original data.")
    

import csv

def calculate_sleep_score(temperature, sound_level, light_level):
    score = 0

    # Check temperature conditions
    if 15 <= temperature <= 20:
        score += 33.333333333  # Increase sleep score by 33.333333333%
    elif temperature == 22:
        pass  # No increase in sleep score if temperature is exactly 22
    
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
    elif temperature == 13:
        advice.append("Low temperature detected. Consider adding blankets for better sleep.")
    elif temperature > 20:
        advice.append("Lower the room temperature to improve sleep.")

    # Light advice
    if light_level > 180:
        advice.append("Dim the lights or use blackout curtains to reduce light exposure.")

    # Sound advice
    if sound_level > 30:
        advice.append("Reduce noise levels by using earplugs or white noise machines.")

    return advice

# Test the sleep score calculation function
def test_sleep_score_calculation():
    sleep_score = calculate_sleep_score(22, 40, 150)
    expected_sleep_score = 33.333333333
    print("Sleep Score:", sleep_score)
    if sleep_score == expected_sleep_score:
        print("Test passed: Sleep score didn't increase when temperature was 22")
    else:
        print("Test failed: Sleep score increased when temperature was 22")
        
test_sleep_score_calculation()

# Test the sleep advice function
def test_sleep_advice():
    advice = get_sleep_advice(13, 20, 150)
    expected_advice = ["Increase the room temperature to improve sleep."]
    print("Advice:", advice)
    if advice == expected_advice:
        print("Test passed: Advice for low temperature provided when temperature was 13")
    else:
        print("Test failed: Advice for low temperature not provided when temperature was 13")

# Run the tests
test_sleep_advice()

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


print("Is sleep time reduced when temperature is high and noise levels are greater than 30dB?")
def reduce_sleep_time(noise_level, temperature, sleep_time):
    if noise_level > 30 and temperature == 'high':
        sleep_time -= 1
    return sleep_time

# Function to convert temperature data
def convert_temperature(temp):
    if temp > 20:
        return 'high'
    elif temp < 15:
        return 'low'
    else:
        return 'normal'

# Read data from CSV file
with open('sleepscore.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get header row
    transposed_data = zip(*reader)  
    for column in transposed_data:
        noise_level = int(column[2])
        temperature = convert_temperature(int(column[1]))
        sleep_time = int(column[4])
        
        new_sleep_time = reduce_sleep_time(noise_level, temperature, sleep_time)
        print("New sleep time:", new_sleep_time)

        

print("Is sleep time reduced if temperature level is low and light levels are greater than 70 standard lux? ")
def reduce_sleep_time(light_level, temperature, sleep_time):
    if light_level > 70 and temperature == 'low':
        sleep_time -= 1
    return sleep_time

# Read data from CSV file
with open('sleepscore.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    transposed_data = zip(*reader)  


for column in transposed_data:
    light_level = int(column[3])
    temperature = column[1]      
    sleep_time = int(column[4])
    
    new_sleep_time = reduce_sleep_time(light_level, temperature, sleep_time)
    print("New sleep time:", new_sleep_time)
 
 
import matplotlib.pyplot as plt

# Data from the provided database
sleep_data = {
    'Day': list(range(1, 31)),
    'Temperature': [13, 28, 14, 27, 27, 27, 26, 26, 26, 13, 26, 14, 26, 26, 26, 26, 26, 26, 25, 26, 14, 25, 12, 13, 25, 25, 25, 14, 25, 25],
    'Sound': [0, 7, 26, 0, 0, 15, 0, 3, 33, 7, 3, 0, 0, 7, 0, 0, 7, 3, 3, 0, 3, 3, 15, 3, 3, 3, 7, 3, 0, 0],
    'Light': [190, 0, 184, 0, 0, 2, 0, 2, 2, 190, 2, 181, 2, 2, 2, 2, 181, 3, 3, 2, 186, 0, 190, 2, 2, 2, 189, 170, 5, 6],
    'Sleep Time': [5, 6, 5, 7, 7, 6, 7, 7, 5, 4, 6, 5, 7, 6, 6, 7, 5, 7, 6, 6, 4, 7, 4, 5, 7, 7, 4, 4, 6, 6]
}

# Plotting
plt.figure(figsize=(10, 6))

plt.scatter(sleep_data['Sleep Time'], sleep_data['Sound'], color='blue', label='Noise Level')
plt.scatter(sleep_data['Sleep Time'], sleep_data['Temperature'], color='red', label='Temperature')

plt.xlabel('Sleep Time')
plt.ylabel('Values')
plt.title('Sleep Time vs Noise Level and Temperature')
plt.legend()

plt.tight_layout()
plt.savefig('sleepscore_plot.png')
plt.show()