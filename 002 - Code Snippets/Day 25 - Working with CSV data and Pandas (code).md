2026-01-03 13:20

Status: Incomplete

Tags: [[Day 25 - Working with CSV and Pandas Library]]

# Code snippets and Examples

```
# import csv

  

# with open("./weather_data.csv") as file:

# data = csv.reader(file)

# temperature = []

# for row in data:

# if row[1] != "temp":

# temperature.append(int(row[1]))

  

# print(temperature)

  

import pandas

  

# data = pandas.read_csv("weather_data.csv")

  

# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()

  

# avg = data["temp"].mean()

# max_temp = data["temp"].max()

  

# print(avg)

# print(max_temp)

  

# # Get Data in columns

# print(data['condition'])

# print(data.condition)

  

# Get Data in the Rows on our DataFrame

# print(data[data.temp == data.temp.max()])

  

# monday = data[data.day == "Monday"]

# print(monday.condition)

# farh = (monday.temp * 1.8) + 32

# print(farh)

  

# Create Datafram from scratch

data_dict = {

"students": ["Amy", "James", "Angela"],

"scores": [76, 56, 65]

}

  

data = pandas.DataFrame(data_dict) # This data can then be converted to other file formats like csv etc...

  

data.to_csv("new_data.csv") # Creates a new csv file with our dataframe

data.to_json("new_data.json") # Creates a new json file with our dataframe
```


### Central Park Squirrel Census data extraction (Extract the count for fur colors)

```
import pandas

  

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260103.csv")

  
  
  

black = len(data[data["Primary Fur Color"] == "Black"])

red = len(data[data["Primary Fur Color"] == "Cinnamon"])

gray = len(data[data["Primary Fur Color"] == "Gray"])

  

# for color in data["Primary Fur Color"]:

# if color == "Black":

# black += 1

# elif color == "Cinnamon":

# red += 1

# elif color == "Gray":

# gray += 1

  

fur_colors_dict = {

"Fur Color": ["Gray", "Cinnamon", "Black"],

"Count": [gray, red, black]

  

}

  

fur_count = pandas.DataFrame(fur_colors_dict)

  

fur_count.to_csv("squirrel_count.csv")

  

print(data[data['Primary Fur Color'] == "Black"])
```



## Reference
[2018 Central Park Squirrel Census Data can be found here](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data_preview)
