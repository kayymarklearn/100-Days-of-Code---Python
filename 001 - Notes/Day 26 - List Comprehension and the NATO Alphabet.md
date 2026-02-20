2026-01-04 18:00

Status: Incomplete

Tags:


# **List Comprehensions**
> It's a case where you create a new list from a previous list.
> ```
> numbers = [1, 2, 3]
> new_list = []
> # Instead of using a for loop.
> # new_list = [new_item for item in list]
> new_list = [n+1 (the new criteria for the new list) for n (any item in our old list) in numbers (our old list)]
> ```

![[List comprehension 1.png]]
> List comprehensions do not only work for lists, they work for other sequences like strings, range, tuples etc.
> ![[List comprehension 2.png]]

> List Comprehension on a range
> ![[List comprehension 3.png]]

> We can also do conditional list comprehension
> It follows the scheme
> new_list = [new_item for item in list if test]
> ![[List comprehension 5.png]]
> test is basically the condition
> ![[List comprehension 6.png]]


# **Dictionary Comprehensions**
> Similar to list comprehensions. Follows the scheme
> new_dict = {new_key:new_value for item in list (or any other iterable)}
> OR
> new_dict = {new_key:new_value for (key, value) in dict.items()}

### Dictionary comprehension from a list
> ![[List comprehension dict.png]]


### Dictionary comprehension from a dictionary
![[List comprehension 7.png]]

## References
