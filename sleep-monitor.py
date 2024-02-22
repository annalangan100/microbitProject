import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM18'
ser.open()
while True:
    data = str(ser.readline())
    
    print("Original data:", data)
    
    data = data.replace("'","")
    data = data.replace("\\r","")
    data = data.replace("\\n","")
    data = data.replace("b","")
    data = data.replace(" ","")
    
    print("Cleaned data:", data)
    
    split_data = data.split(":")
    print("Split data:", split_data)
    temperature_data = int(split_data[1])
    light_data = int(split_data[3])
    sound_data = int(split_data[5])
    
    print("Seperated data")
    print("Temp: ", temperature_data, "type", type(temperature_data))
    print("Light: ", light_data, "type", type(light_data))
    print("Sound: ", sound_data, "type", type(sound_data))
          
    print()
    
    
    
    