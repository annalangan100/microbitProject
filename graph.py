import csv
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
