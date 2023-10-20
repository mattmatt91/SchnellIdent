import requests



# url = f"http://127.0.0.1:3000/measurement"
# response_id = requests.get(url)
# print(response_id.json())
# 
# 
# 
# url = f"http://127.0.0.1:3000/get_all_measurements"
# response = requests.get(url)
# print(response.json())

response_id = "f2e20dd3-4909-4d02-b4bf-6cfab9cb1030"
url = f"http://127.0.0.1:3000/get_dataset/{response_id}"
response = requests.get(url)
print(response.json())