2026-01-19 21:50

Status: Incomplete

Tags: [[Day 30 - Errors and Exceptions (Code)]]


# **Errors and Exceptions**
## Handling Errors and Exceptions
> Catching Exceptions:
> ```
> try:
> 	executing a block of code that might cause an exception
> except:
> 	block of code to execute if there is an exception (error)
> else:
> 	block of code to run if there was no exception (error)
> finally:
> 	block of code to run no matter what happens.
> 	raise KeyError # Raise a KeyError no matter what
> ```
> Raising Exceptions:
> ```
> #raise: 
> 	#used to raise an exception
> 	
> ```

## JSON Data
> In Python we use the Json module to work on json data and files; its built in so use `import json` to use
> ```
> with open('data.json', 'w') as file:
> 	# Use json.dump() to write data to the json file
> 	# json.dump takes three ags
> 		- a dict data
> 		- the file name
> 		- indent= to make the data more human readable
> 		- json.dump(new_dict, file_name, indent=4)
> 	# json.load(): takes the arg; name of json file
> 	# basically returns the data as a dictionary
> 	# data = json.load(file_name)
>
>	# json.update(): Used to update the data in a json file
>	# We first load the data before updating it
>	# data = json.load(data_file)
>	# data.update(new_data)
>	# json.dump(data, data_file, indent=4)
> ```



## References
