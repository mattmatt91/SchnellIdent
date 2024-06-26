import pandas as pd
import random
import requests
import os

IP_DAQ = os.getenv("IP_DAQ", "default_ip")
PORT_DAQ = os.getenv("PORT_DAQ", 8500)

def command_daq(daq_arguments: dict):
    url = f"http://{IP_DAQ}:{PORT_DAQ}/sensor_data"
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
        "duration_heater": 0,
        "channel_ir": 2,
        "channel_mic": 1
    }

    data = command_daq(daq_arguments)
    print(data)
