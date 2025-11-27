2025-11-27 20:14

Status: Complete
 
Tags: [[Day 9 - Dictionaries and Nesting]] [[Day 9 - Secret Auction Program]]

# Code snippets and Examples

> This is how you create a dictionary in Python:
```
# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}
```

> This is how you retrieve items from a dictionary:

```
print(colours["pear"])
#Will print "green"
```

> This is how to create an empty dictionary:
```
my_empty_dictionary = {}
```
> It's possible to wipe a dictionary by reassigning it to empty dictionary as above


> This is how you can add new items to an existing dictionary:
`colours["peach"] = "pink"`

> This is also how you can edit an existing value in a dictionary:
> ```
> colours["apple"] = "green"
> ```

> This is how to loop through a dictionary and print all the keys:

```
for key in colours:
    print(key)
```

> This is how to loop through a dictionary and print all the values:
```
for key in colours:
    print(colours[key])**
```

> Trying to access data that is not in the dictionary we get a #KeyError

### Nesting
> Nesting a list in a dictionary
```
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1]) # prints out Lille
```

> Nesting Lists inside other Lists
```
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1]) # Prints out D
```

> Nesting a dictionary inside a dictionary
```
my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
```

```
travel_log = {  
  "France": {  
    "cities_visited": ["Paris", "Lille", "Dijon"],  
    "total_visits": 12  
   },  
  "Germany": {  
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  
    "total_visits": 5  
   },  
print(travel_log["Germany"]["cities_visited"][2]) # prints out Stuttgart
```