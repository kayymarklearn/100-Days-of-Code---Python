#TypeError
> Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.


#ValueError 
> Raised when an operation or function receives an argument that has the right type but an inappropriate value.


#IndentationError 
> Base class for #SyntaxError  related to incorrect indentation


#SyntaxError
> Raised when the parser encounters a syntax error.

#IndexErrors
> Raised when you use an index that is larger than the size of your list
> #Example calling for fruits\[3]
> When fruits has just 3 items \[Remember we count from zero]

#KeyError 
> providing wrong key or a key does not exist in a dictionary, it also happens when using a key with different data type.

### Nesting
> You can mix and match various data types to achieve your desired structure.
 Nesting a List inside a Dictionary
Instead of a String value assigned to a key, we can replace it with a List. You can nest a List in a Dictionary like this:
```
my_dictionary = {
    key1: [List],
    key2: Value,
}
```

## References
[Python Documentation](https://docs.python.org/3/)
[IndexError](https://docs.python.org/3/library/functions.html#len)

