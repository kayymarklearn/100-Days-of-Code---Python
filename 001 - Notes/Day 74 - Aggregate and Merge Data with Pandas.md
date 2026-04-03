2026-03-29 21:34

Status: Incomplete

Tags: [[Day 72 - Data Exploration with Pandas]]
[[Day 73 - Data Visualization with Matplotlib]]

##### Finding the number of unique categories.
To find the number of unique category in a column, you can use the `.nunique()` method.
```Python
dataframe['column_name'].nuniqe()
```

##### Finding the number of values in of each category in a column you can use two methods
- `groupby()` method:
	```Python
	dataframe.groupby('column_name').count()
	```
- `value_counts()` method:
	```Python
	dataframe.column_name.value_counts()[Category]
	# example
	false_count = lego_colors.is_trans.value_counts()[False]
	
	# OR
	true_count = (lego_colors['is_trans'] == True).sum()

	true_count
	```


#### Aggregating data
Often you find yourself needing to summarise data. This is where the .groupby() function comes in really handy. However, sometimes you want to run even more operations based on a particular DataFrame column. This is where the [.agg()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html) method comes in.


#### Merging dataframes
the [.merge() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge) to combine two separate DataFrames into one. The merge method works on columns with the same **name** in both DataFrames.

Currently, our theme_ids and our number of sets per theme live inside a Series called `set_theme_count`.

#Note The cells inside jupyter can be code cells or markdown cells.
#Note The `.agg()` method takes a dictionary as an argument. In this dictionary, we specify which operation we'd like to apply to each column.

#### Today's learning points

- use HTML Markdown in Notebooks, such as section headings # and how to embed images with the <img> tag.

- combine the groupby() and count() functions to aggregate data

- use the .value_counts() function

- slice DataFrames using the square bracket notation e.g., df[:-2] or df[:10]

- use the .agg() function to run an operation on a particular column

- rename() columns of DataFrames

- create a line chart with two separate axes to visualise data that have different scales.

- create a scatter plot in Matplotlib

- work with tables in a relational database by using primary and foreign keys

- .merge() DataFrames along a particular column

- create a bar chart with Matplotlib



## References
[Value_counts method docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html)
[Nunique method docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html#pandas.DataFrame.nunique)
[sort_values method docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values)
[groupby method docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby)
[.agg method docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html)

[Scatter plot in matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
[merge method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge)
