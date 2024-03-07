import csv

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

        
        
import csv

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
