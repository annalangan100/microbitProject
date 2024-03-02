import csv

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
    next(reader)  # Skip header row
    for row in reader:
        noise_level = int(row[3])
        temperature = convert_temperature(int(row[2]))
        sleep_time = int(row[4])
        
        new_sleep_time = reduce_sleep_time(noise_level, temperature, sleep_time)
        print("New sleep time:", new_sleep_time)
        
        
import csv

def reduce_sleep_time(light_level, temperature, sleep_time):
    if light_level > 70 and temperature == 'low':
        sleep_time -= 1
    return sleep_time

# Read data from CSV file
with open('sleepscore.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        light_level = int(row[3])
        temperature = row[1]  # Assuming temperature data is already formatted as 'low' or 'high'
        sleep_time = int(row[4])
        
        new_sleep_time = reduce_sleep_time(light_level, temperature, sleep_time)
        print("New sleep time:", new_sleep_time)

