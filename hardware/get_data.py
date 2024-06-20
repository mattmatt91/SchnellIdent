import pandas as pd
import random
import requests

def command_daq(daq_arguments:dict):
    base_url="http://daq:5000/sensor_data"
    response = requests.get(base_url, params=daq_arguments)

    if response.status_code == 200:
        data = response.json()
        if all(key in data for key in ("IR", "MIC", "TIME")):
            return data
        else:
            raise ValueError("Response JSON does not contain the required keys.")
    else:
        response.raise_for_status()

    new_data = pd.DataFrame(data)
    return new_data.to_dict(orient='list')

def eval_data(data:pd.DataFrame):
    key = "pos" if random.choice([True, False]) else "neg"
    result = True if key  == "pos" else False




# Example usage
if __name__ == "__main__":
    sampling_rate = 10000  # Example sampling rate
    duration =     3    # Example duration in seconds

    data = command_daq(sampling_rate, duration)
    print(data)





