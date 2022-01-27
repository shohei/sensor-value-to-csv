import serial
import time # Optional (required if using time.sleep() below)
import sys
import os
import pandas as pd
from datetime import datetime

port = "/dev/tty.usbmodem142301"
ser = serial.Serial(port=port, baudrate=9600)

class DataCapture():
    def __init__(self):
        self.lines = ""
        self.filename = datetime.now().strftime("%d%m%y_%H%M%S")+".csv"
        self.data_dict = {"pressure":[], "airflow":[], "oilflow":[]}
        df = pd.DataFrame(self.data_dict)
        df.to_csv(self.filename, mode='w', index=False)

    def main(self):
        while (True):
            if (ser.inWaiting() > 0):
                data_str = ser.read(ser.inWaiting()).decode('ascii') 
                #print(data_str, end='') 
                self.lines += data_str.rstrip()
                if "\n" in data_str:
                    output = self.lines.split(",")
                    pressure = output[0]
                    airflow = output[1]
                    oilflow = output[2]
                    print(f"data received:{output}")
                    self.data_dict["pressure"].append(pressure)
                    self.data_dict["airflow"].append(airflow)
                    self.data_dict["oilflow"].append(oilflow)
                    df = pd.DataFrame(self.data_dict)
                    df.to_csv(self.filename, mode='a', index=False, header=False)

                    self.reset()
             
            time.sleep(0.01) #100Hz

    def reset(self):
        self.lines = ""
        self.data_dict["oilflow"] = []
        self.data_dict["airflow"] = [] 
        self.data_dict["pressure"] = []

if __name__=="__main__":
    d = DataCapture()
    try:
        d.main()
    except KeyboardInterrupt:
        print("Interrupted.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
