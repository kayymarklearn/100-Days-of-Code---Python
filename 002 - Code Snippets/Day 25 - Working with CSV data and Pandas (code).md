
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

### Iterating through dictionaries and pandas DataFrames
```
student_dict = {

"student": ["Angela", "James", "Lily"],

"score": [56, 76, 98]

}

  

#Looping through dictionaries:

for (key, value) in student_dict.items():

#Access key and value

pass

  

import pandas

student_data_frame = pandas.DataFrame(student_dict)

  

#Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():

#Access index and row

#Access row.student or row.score

pass

  

# Keyword Method with iterrows()

# {new_key:new_value for (index, row) in df.iterrows()}
```

### More pandas examples
```
import pandas as pd

  

df = pd.read_csv("orders.csv") # type: ignore

  

# Indexing based on columns (series)

# print(df[["Country", "Product", "Quantity"]])

  

# Get the range for the rows

# Get first five rows

# print(df.head())

# Get last five rows

# print(df.tail())

# Get all column names

# print(df.columns)

# Get info or math data on data

# (print(df.info())) # Verbose info

# print(df.describe()) # Verbose math data (max, count, mean, std, min, 25%, 50%, 75%)

# print(df.index)

# Indexing based on rows (series)

# print(df.iloc[1]) # Access data using the row index

# for i in range(0, 40, 1):

# print(f"{i}. {df.iloc[i]["CustomerName"]}\n{df.iloc[i]["Country"]}")

  

# Filtering data

  

# print(df[(df["Category"] == "Electronics") & (df["Country"] == "USA")]) # Look for all values where the category is electronics and the country is USA

# print(df[(df["Category"] == "Electronics")| (df["Country"] == "USA")]) # Look for all entries where the category is Electronics or the country is USA

  

# print(df[df["Quantity"] > 20]) # All entries where Quantity is greater than 20 [Basically all conditions can be checked]

# print(df[df["Quantity"] != 2]) # All entries where Quantity is not 2

  

# print(df[df["CustomerName"].str.startswith("A")]) # Check for all Customer Names that starts with A

# print(df[df["CustomerName"].str.endswith("s")]) # All customer Names that ends with s

# print(df[df["Country"].isin(["USA", "Sweden", "Brazil"])]) # Check if an entry is in a given list (array)

# print(df[~df["Country"].isin(["USA", "Sweden", "Brazil"])]) # The tild ~ operator reverses the condition just like not (!)

  

# Updating data

  

# print(df.loc[df["CustomerName"] == "Anna Ivanova"]) # Accessing using the column name

# df.loc[df['CustomerName'] == "Nora Ibrahim", "Product"] = "Laptop" # Find an entry using the name and update the row

# print(df.loc[df["CustomerName"] == "Nora Ibrahim"])

  

# df.loc[df['Country'] == "USA", "Country"] = "United States" # Update USA to United States in the country column for all entries

# df["Country"] = df["Country"].str.upper() # Change everything in a column (in this case make it all upper case)

# print(df["Country"])

  
  

# Deleting data

# df = df.drop(39) # Delete row at index 39

# print(df.tail())

  

# Cleaning data

# df.dropna(inplace=True) # Drop any data with null data

  

# df.fillna({"OrderID": 0}, inplace=True) # replace all OrderIDs with no data with 0 and replace in the current df not return a new df (inplace)

  
  

# Renaming columns

# print(f"{df.head()}\n")

# df.rename(columns={"OrderID": "Order ID"}, inplace=True) # replaces a column name in the df without returning a new one

# print(df.head())

  

# Analyzing Data

# print(df["Country"].value_counts()) # Return a count of every value in the given column

# print(df.groupby("Country")["Price"].sum()) # Group by a given column data, like sorting in excel

# print(df.sort_values("Price", ascending=False)) # sort in descending order by price (takes inplace to determine if it'll affect the dataframe)

# print(df.sort_values("Quantity", ascending=True)) # sort in ascending order of quantity (smallest to largest)

  

df.sort_values("Price", ascending=False, inplace=True)

  

df.to_csv("new_file.csv", index=False) # Save to a new csv file, without index (use True if keeping index or don't add an index arg)
```

## Reference
[2018 Central Park Squirrel Census Data can be found here](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data_preview)
