2026-03-28 10:33

Status: incomplete

Tags: [[Day 25 - Working with CSV and Pandas Library]]
[[Day 73 - Data Visualization with Matplotlib]]

# **Pandas**
Pandas is one of the most popular python packages for working with data as we already learned in Day 25.
In our notebook import pandas and read the file using the `pandas.read_filetype` method.
For a csv file, it'll be
```Python
import pandas
df = pandas.read_csv("filename.csv")
```
This creates a pandas dataframe with name df.
When importing from csv, we can substitute the column names with the names argument, and setting the header row to zero.
```Python/pandas
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
```

We can take a look at the first 5 rows by using the `.head()` method on our dataframe. Similarly we can use the `.tail()` method to see the last couple of rows.
`df.head() # df is the name of the dataframe we created` 
![[Pasted image 20260328105400.png]]

Once we have our data loaded into a dataframe, we need to look closer to help us understand what it is we are working with. This is always the first step with any data science project. Let's see if we can answer the questions.
> - How many rows does our dataframe have?
> - How many columns does it have
> - What are the labels of the columns? Do the columns have names?
> - Are there any missing values in our dataframe? Does our dataframe contain any bad data?


To answer our questions above, we have already used the .head() method to peek at the top 5 rows of our dataframe. 
- To see the number of rows and columns, we can use the *shape* attribute.
![[Pasted image 20260328105743.png]]
	This tells us that our dataframe has 51 rows and 6 columns.


- We can access the column names directly with the *columns* attribute.
![[Pasted image 20260328105652.png]]
	This returns all the column names in a dataframe.

#### Missing Values and Junk Data
Before we can proceed with our analysis we should try and figure out if there are any missing or junk data in our dataframe. That way we can avoid problems later on. In this case, we're going to look for NaN (Not A Number) values in our dataframe. NAN values are blank cells or cells that contain strings instead of numbers. 
We use the `.isna()` method to spot any potential problems or junk data.
![[Pasted image 20260328110230.png]]

###### Delete the Last Row
We don't want this row in our dataframe. There's two ways you can go about removing this row. The first way is to manually remove the row at index 50. The second way is to simply use the `.dropna()` method from pandas. Let's create a new dataframe without the last row and examine the last 5 rows to make sure we removed the last row:
![[Pasted image 20260328110445.png]]

##### Accessing Columns from dataframe
To access a particular column from a data frame we can use the square bracket notation, like so:
```Python
clean_df['Column Name']
# For column names with no spaces we can use the dot notation
clean_df.NAME[1] # accesses the first row of column NAME
```
![[Pasted image 20260328110802.png]]
	We can chain methods to this to get specific data
	- To find the highest salary, we can chain the `.max()` method like so,
		`clean_df['Starting Median Salary'].max()`
		![[Pasted image 20260328111022.png]]
The highest starting salary is $74,300. But which college major earns this much on average? For this, we need to know the row number or **index** so that we can look up the name of the major. Lucky for us, the `.idxmax()` method will give us index for the row with the largest value. This will return the index of the row with the highest starting median salary.
	```Python
		clean_df['Starting Median Salary'].idxmax()
		# returns row index [43] in this instance
	```
To see the name of the major that corresponds to that particular row, we can use the `.loc` (location) property.
`clean_df['Undergraduate Major'].loc[43]`
Here we are selecting both a column ('Undergraduate Major') and a row at index 43, so we are retrieving the value of a particular cell. You might see people using the double square brackets notation to achieve exactly the same thing: 
`clean_df['Undergraduate Major'][43]`
![[Pasted image 20260328112017.png]]

If you don't specify a particular column you can use the .loc property to retrieve an entire row:

`clean_df.loc[43]`
![[Pasted image 20260328112153.png]]

#Note We can also nest code when searching for data
`clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmax()]`

##### Lowest Risk Majors
A low-risk major is a degree where there is a small difference between the lowest and highest salaries. In other words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small, then you can be more certain about your salary after you graduate.
How would we calculate the difference between the earnings of the 10th and 90th percentile? Well, Pandas allows us to do simple arithmetic with entire columns, so all we need to do is take the difference between the two columns:

```Python
clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
```

Alternatively, you can also use the `.subtract()` method.
```Python
clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
```

The output of this computation will be another Pandas dataframe column. We can add this to our existing dataframe with the `.insert()` method:
```pandas
spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

clean_df.insert(1, "Spread", spread_col)
clean_df.head()
```
The first argument is the position of where the column should be inserted. In our case, it's at position 1, so the second column.

##### Sorting by the lowest spread
To see which careers have the smallest spread, we can use the `.sort_values()` method. And since we are interested in only seeing the name of the degree and the major, we can pass a list of those two column names to look at the `.head()` of these two columns exclusively. 
```Pandas
low_risk = clean_df.sort_values("Spread")
low_risk[['Undergraduate Major', 'Spread']].head()
```

##### Getting Careers with the highest potential
```Python/pandas
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Spread']].head()
```
You can specify whether `.sort_values()` method should sort in ascending order or not by specifying the ascending argument, default is True.

##### Majors with the highest spread in Salary
```Python/pandas
highest_spread = clean_df.sort_values("Spread", ascending=False)
highest_spread[['Undergraduate Major', 'Spread', 'Group']].head()
```

#### Grouping and Pivoting Data with Pandas
Often times you will want to sum rows that belong to a particular category. For example, which category of degrees has the highest average salary? Is it STEM, Business or HASS (Humanities, Arts, and Social Science)?
To answer this question we need to learn to use the `.groupby()` method. This allows us to manipulate data similar to a Microsoft Excel Pivot Table.

We have three categories in the 'Group' column: STEM, HASS and Business. Let's count how many majors we have in each category:

`clean_df.groupby('Group').count()`

We can use the `.mean()` method to find the average salary by group.
`clean_df.groupby('Group').mean()`

##### Number Formats in the output
The above is a little hard to read, isn't it? We can tell Pandas to print the numbers in our notebook to look like 1,012.45 with the following line:

`pd.options.display.float_format = '{:,.2f}'.format`

### Today's Learning Points
- Use `.head()`, `.tail()`, `.shape` and `.columns` to explore your DataFrame and find out the number of rows and columns as well as the column names.
    
- Look for NaN (not a number) values with `.findna()` and consider using `.dropna()` to clean up your DataFrame.
    
- You can access entire columns of a DataFrame using the square bracket notation: `df['column name']` or `df[['column name 1', 'column name 2', 'column name 3']]`
    
- You can access individual cells in a DataFrame by chaining square brackets `df['column name'][index]` or using `df['column name'].loc[index]`
    
- The largest and smallest values, as well as their positions, can be found with methods like `.max()`, `.min()`, `.idxmax()` and `.idxmin()`
    
- You can sort the DataFrame with `.sort_values()` and add new columns with `.insert()`
    
- To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the `.groupby()` method.

#### Tools
- Google Colab Notebook
- Anaconda


## References
[Sort values Docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)
