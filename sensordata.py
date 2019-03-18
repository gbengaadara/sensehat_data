from sense_hat import SenseHat
from datetime import datetime
from csv import writer


# Creating a file for writing Sensehat data to

import csv


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

    return sense_data

with open('sensedata.csv', 'w', newline='') as f:
    data_writer = writer(f)

    while True:
            print(get_sense_data())

            # write output to file

            data = get_sense_data()
            data_writer.writerow(data)
