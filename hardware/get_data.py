import pandas as pd
import random
import requests
import os


REACT_APP_IP_DAQ= "192.168.2.100" # os.getenv("REACT_APP_IP_DAQ", "192.168.1.52")
REACT_APP_PORT_DAQ = 8500 # os.getenv("REACT_APP_PORT_DAQ", 8500)

def command_daq(daq_arguments: dict):
    url = f"http://{REACT_APP_IP_DAQ}:{REACT_APP_PORT_DAQ}/sensor_data"
    response = requests.post(url, json=daq_arguments)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        response.raise_for_status()


# Example usage
if __name__ == "__main__":
    
    daq_arguments = {
        "rate": 10000,
        "duration": 3,
        "power": 5,
        "offset_heater":0.5,
        "duration_heater": 1,
        "channel_ir": 2,
        "channel_mic": 1
    }

    data = command_daq(daq_arguments)
  
