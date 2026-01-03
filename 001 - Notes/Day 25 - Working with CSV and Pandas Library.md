2026-01-03 11:56

Status: Incomplete

Tags: [[Day 25 - Working with CSV data and Pandas (code)]]


# **CSV**
> CSV is short for Comma separated values and its a simple way of representing tabular data (like in xcel) using only commas.
> Each piece of data without spaces.
> They can be manipulated in python using normal file operations.
> But python also has a special module called (CSV) for working with csv files.
> CSV module is good for working with small pieces of data but inefficient for large amounts.
> For large datasets, we use Pandas
> ```
> import csv
> with open("data.csv") as file:
> 	data = csv.reader(file) # Returns a list of all the csv rows
> ```

·
# **pandas**
> Read the documentation from #Reference
> Pandas automatically reads the csv file and formats it.
> ```
> import pandas
 data = pandas.read_csv("weather_data.csv")
print(data) # prints the entire table
print(data["temp"]) # Uses the first row as the the name of the column
> ```
> In pandas a tabular data (excel, csv, json, db etc) is called a DataFrame while  columns in the DataFrame are called a Series (kinda like a list)


## References
[Pandas documentation](https://pandas.pydata.org/docs/)
[Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)
