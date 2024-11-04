import requests
import json
import os
import pandas as pd
import plotly.express as px
from datetime import datetime


def read_params():
    with open('config.json', 'r') as file:
        params = json.load(file)
    return params

params = read_params()
params_host_daq = params["HOST"]
params_measurement = params["MEASUREMENT"]

def test_sensor_data_api():
    url = f"http://{params_host_daq['HOST_DAQ']
                    }:{params_host_daq['PORT_DAQ']}/sensor_data"

    # Send a POST request with the parameters as JSON
    print(params_measurement)
    response = requests.post(url, json=params_measurement)
    # print(response.json())
    # Print the response from the server
    print("Status Code:", response.status_code)
    return response.json()


def plot_data(data: pd.DataFrame, subfolder: str):
    fig = px.line(data, x="time", y=["MIC", "IR"],)
    fig.update_layout(xaxis_title="Time", yaxis_title="Sensor Readings")
    html_filename = os.path.join(subfolder, "sensor_data_plot.html")
    fig.write_html(html_filename)
    print(f"HTML plot saved to: {html_filename}")


def save_data(data):
    # print(data)
    df = pd.DataFrame(data)
    df["time"]= [(1/params_measurement["rate"])*i for i in df.index]
    # Ensure the data subfolder exists and create a timestamped subfolder
    data_folder = "data"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    subfolder = os.path.join(data_folder, timestamp)
    os.makedirs(subfolder, exist_ok=True)

    # Save the DataFrame as a CSV file in the subfolder
    csv_filename = os.path.join(subfolder, "sensor_data.csv")
    df.to_csv(csv_filename, index=False)
    print(f"CSV file saved to: {csv_filename}")
    # Create a Plotly line plot
    plot_data(df, subfolder)
    

if __name__ == "__main__":
    response_data = test_sensor_data_api()
    print(response_data)
    # data = save_data(response_data)

