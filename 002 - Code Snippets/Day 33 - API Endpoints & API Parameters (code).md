2026-01-25 19:16

Status: Incomplete

Tags:  [[Day 33 - API Endpoints & API Parameters]]

# Code snippets and Examples
```
# Simple Get request
import requests
response = requests.get("http://api.open-notify.org/iss-now.json")

print(response) # Prints the response code
```

### Finding the ISS position using the notif API
```
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

response.raise_for_status() # Raise an exception if the request returns an unsuccesful request code (200)

data = response.json() # Actual data returned by the response

print(data)

print(data['timestamp']) # We can tap in the data using keys just like python dictionaries

longitude = data['iss_position']['longitude']

latitude = data['iss_position']['latitude']

  

iss_position = (longitude, latitude)

  

print(iss_position)
```


### API calls with parameters (Sunset and Sunrise API)
```
import requests

from datetime import datetime

MY_LAT = 34.972230

MY_LONG = -0.023445


#........................... Request with parameters ........................ #

  

parameters = {

'lat': MY_LAT,

'lng': MY_LONG,

'formatted': 0

} # parameters must have same names as specified in API docs

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise']

sunset = data['results']['sunset']

print(f"Sunrise: {sunrise.split("T")[1].split(":")[0]}")

print(f"Sunset: {sunset.split("T")[1].split(":")[0]}")

time_now = datetime.now()

print(f"Time Now: {time_now.hour}")
```