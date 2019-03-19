from sense_hat import SenseHat
from datetime import datetime
from csv import writer


# Creating a file for writing Sensehat data to

import csv

# get the delay in seconds
delay = int(input("Enter delay between readings in seconds: "))

# get the filename to write to
filename = input("Enter the name of output file: ")

timest = datetime.now()
# delay = 1

sense = SenseHat()

def get_sense_data():
    sense_data = []

    # added round to round the data to 2 decimal places
    
    sense_data.append(round(sense.get_temperature(), 2))
    sense_data.append(round(sense.get_pressure(), 2))
    sense_data.append(round(sense.get_humidity(), 2))

    # Get the date time and format for Y-M-D T
    # print datetime out as a string
    
    now = datetime.now()
    sense_data.append(str(now.strftime("%Y-%m-%d %H:%M")))

    # Get the time again, but in a format we can use to calculate delay
    sense_data.append(now)

    return sense_data
# Write the values to a file
with open(filename, 'w', newline='') as f:
    data_writer = writer(f)

    # Wite csv headers
    data_writer.writerow(["Temp", "Pressure", "Humidity", "Time"])
    
    
    while True:
        
          
        # write output to file

        data = get_sense_data()

        dt = data[-1] - timest
        
        if dt.seconds > delay:
            # Write only the first 4 elememts, we do not need the 5th as we only used for calculation
            data_writer.writerow(data[0:4])
            # print(data[0],",",data[1],",",data[2])
            # print(data[0:4])
            timest = datetime.now()
