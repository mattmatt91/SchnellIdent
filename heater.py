import requests



url_heater = 'https://w3schools.com/python/demopage.htm'

def toggle_heater(duration:int, power:int):
    x = requests.get(url_heater)
    print(x.text)
    