2026-04-03 20:44

Status: Incomplete

Tags: [[Day 76 - Plotly Charts]]
[[Day 75 - Google Trends Data Resampling]]
[[Day 74 - Aggregate and Merge Data with Pandas]]
[[Day 78 - Linear Regression and Data visualization with Seaborn]]
# **Numerical Python (Numpy)**
Numpy is a Python library that's used in almost every field of science and engineering. It's practically the stand for working with numerical data in python. Libraries like Pandas are built on numpy.


### Ndarray
The crown jewel of NumPy is the ndarray. The ndarray is a homogenous n-dimensional array object. This simply means that all the data in the array have the same data type. And n-dimensional means that we can work with everything from a single column (1-dimensional) to the matrix (2 dimensional) to a bunch of matrices stacked on  top of each other (n-dimensional).
##### 1-Dimension
We can create a 1-d array (i.e. a 'vector') by passing a list to the numpy.array method
```Python
import numpy as np
one_d_array = np.array([1, 2 ,3 ,4 ,5])
```
We can check the shape (columns, rows) of an array by using the `.shape` attribute of that array object, which returns the number of columns in the array. The `.ndim` attribute returns the dimensions of the array, so 1 for a 1d array and 2 for a 2d array and so forth.

We can access elements of the array just like how we access python lists, namely buy  that element's index:
`one_d_array[2]` for the third element (0-based).

##### 2-dimensions
#Note NumPy refers to dimensions as axes.
To access an element in 2d array, we have to give it index for each dimension. We have 2 dimensions so we need to provide an index for the row and for the column. Here's how to access the 3rd value in the 2nd row:
```Python
my_2d_array[1, 2]
```

Access an entire row and all the values therein, you can use the : operator just like in python lists.
Here's the entire first row:
`array_2d[0, :]`

Here's the entire 3rd column
`array_2d[:, 2]`


##### N-Dimensions 
An array of 3-dimensions (or higher) is often referred to as a 'tensor'. That’s also where Tensorflow, the popular machine learning tool, gets its name. A tensor simply refers to an n-dimensional array.
#Note to reverse the order of an array use the `.flip()` method or the the python list double colon `[::-1]`
```
a = np.array([1, 2, , 3, 4, 5])
np.flip(a)
# OR
a[::-1]
```

#Note The `np.nonzero` function returns a tuple of the indices of all non-zero numbers in an array
```Python
b = [6, 0, 9, 0, 0, 5, 0]
nz_indices = np.nonzero(b)
nz_indices # This is a tuple
```

#Note You can create an array with random numbers by using the `random` function by importing it from `numpy.random`

```Python
from numpy.random import random

z = random((3, 3, 3)) # Creates a n array with the dimensions given in the tuple
# OR you could use the full path
z = np.random.random((3,3,3)) # without importing it.
z # Will return a 3X3 array with random floats between 0 and 1
print(z.shape)
```
#Note Other useful functions to learn `.linspace()`

### Linear Algebra with vectors
NumPy is designed to do math (and do it well!). This means that NumPy will treat vectors, matrices and tensors in a way that a mathematician would expect. For example, if you had two vectors:
```Python
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
```
And you add them together
`v1 + v2`
The result will be a ndarray where all the elements have been added together.
`array([ 6, 6, 5, 10])`
In contrast, if we add two python lists, adding them will concatenate the lists. This causes a #TypeError 
We can also multiply arrays in this manner.

#####  Broadcasting
Oftentimes you'll want to do some sort of operation between an array and a single number. In mathematics, this single number is often called a **scalar**. For example, you might want to multiply every value in your NumPy array by 2:
![[Pasted image 20260403221122.png]]

In order to achieve this result, NumPy will make the shape of the smaller array - our scalar - compatible with the larger array. This term is referred to as broadcasting in the numpy documentation
The same rules about 'expanding' the smaller ndarray hold true for 2 or more dimensions.

##### Matrix Multiplication
But what if we're not multiplying our ndarray by a single number? What if we multiply it by another vector or a 2-dimensional array? In this case, we follow [the rules of linear algebra](https://en.wikipedia.org/wiki/Matrix_multiplication#Illustration).
We use the `.matmul()` method or the `@` operator
```Python
a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

c = np.matmul(a1, b1) 
# OR
c = a1 @ b1

# both result in 
%% array([[19, 25, 18],
       [ 5,  8,  5],
       [34, 22, 28],
       [71, 65, 62]]) %%
```


#### Manipulating Images as ndarrays
Images are nothing other than a collection of pixels. And each pixel is nothing other than value for a colour. And any colour can be represented as a combination of red, green, and blue (RGB).
The python libraries `Scipy` and `PIL` allow us to work with images.
#Note Images are essentially ndarrays


### Today's Learning Points
In today's lesson I looked at how to:

- Create arrays manually with `np.array()`
    
- Generate arrays using  `.arange()`, `.random()`, and `.linspace()`
    
- Analyse the shape and dimensions of a ndarray
    
- Slice and subset a ndarray based on its indices
    
- Do linear algebra like operations with scalars and matrix multiplication
    
- Use NumPys broadcasting to make ndarray shapes compatible
    
- Manipulate images in the form of ndarrays

## References
