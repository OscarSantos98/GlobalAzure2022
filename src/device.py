import json
import random
import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# Create random values for temperature and add them to the list
temperature_list = []

for i in range(1, 4):

    temperature_dict = dict()
    temperature = random.randint(0, 60)
    temperature_dict["driveGearId"] = i
    temperature_dict["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature_dict["temperature"] = temperature
    temperature_list.append(temperature_dict)
    
# print(temperature_list)
readings = dict()
readings['readings'] = temperature_list

# Send a POST request to the server with the temperature list
url = 'https://azfunctiondemotest1.azurewebsites.net/api/HttpTrigger1'
headers = {'Content-Type': 'application/json',
           'x-functions-key': os.environ.get('FUNCTION_KEY')}
data = json.dumps(readings)
print(data)
response = requests.post(url, data=data, headers=headers)

if response.status_code == 200:
    print(response.text)

