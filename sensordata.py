from sense_hat import SenseHat
from datetime import datetime

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

while True:
    print(get_sense_data())
