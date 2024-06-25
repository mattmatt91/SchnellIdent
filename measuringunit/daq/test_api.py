import requests
PORT_DAQ = 8500
IP_DAQ = "192.168.1.52"

def test_sensor_data_api():
    url = f"http://{IP_DAQ}:{PORT_DAQ}/sensor_data"
    # Define the parameters for the request
    params = {
        "rate": 10000,
        "duration": 2.0,
        "power": 0.5,
        "duration_heater": 0.5,
        "channel_ir": 0,
        "channel_mic": 1
    }
    # Send a POST request with the parameters as JSON
    response = requests.post(url, json=params)
    
    # Print the response from the server
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    test_sensor_data_api()
