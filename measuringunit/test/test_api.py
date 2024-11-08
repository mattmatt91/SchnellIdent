import requests
import json
import os
import pandas as pd
import plotly.express as px
from datetime import datetime

# Custom adapter to bind to a specific IP address
class LocalBindAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, local_addr, **kwargs):
        self.local_addr = local_addr
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs['source_address'] = (self.local_addr, 0)  # 0 for any available port
        super().init_poolmanager(*args, **kwargs)

def read_params():
    with open('config.json', 'r') as file:
        params = json.load(file)
    return params

params = read_params()
params_host_daq = params["HOST"]
params_measurement = params["MEASUREMENT"]

def test_sensor_data_api():
    url = f"http://{params_host_daq['HOST_DAQ']}:{params_host_daq['PORT_DAQ']}/sensor_data"

    # Create a session and bind it to the Ethernet IP
    session = requests.Session()
    session.mount("http://", LocalBindAdapter(f"{params_host_daq['USE_IP']}"))

    # Send a POST request with the parameters as JSON
    print(params_measurement)
    response = session.post(url, json=params_measurement)
    print("Status Code:", response.status_code)
    return response.json()

def plot_data(data: pd.DataFrame, subfolder: str):
    fig = px.line(data, x="time", y=["MIC", "IR"])
    fig.update_layout(xaxis_title="Time", yaxis_title="Sensor Readings")
    html_filename = os.path.join(subfolder, "sensor_data_plot.html")
    fig.write_html(html_filename)
    print(f"HTML plot saved to: {html_filename}")

def save_data(data):
    df = pd.DataFrame(data)
    df["time"] = [(1/params_measurement["rate"]) * i for i in df.index]
    data_folder = "data"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    subfolder = os.path.join(data_folder, timestamp)
    os.makedirs(subfolder, exist_ok=True)

    csv_filename = os.path.join(subfolder, "sensor_data.csv")
    df.to_csv(csv_filename, index=False)
    print(f"CSV file saved to: {csv_filename}")
    plot_data(df, subfolder)

if __name__ == "__main__":
    response_data = test_sensor_data_api()
    print(response_data)
    save_data(response_data)
