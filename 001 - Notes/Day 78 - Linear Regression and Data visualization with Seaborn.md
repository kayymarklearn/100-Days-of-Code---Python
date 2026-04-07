2026-04-04 00:40

Status:

Tags:
[[Day 77 - Computation with Numpy and N-Dimensional Arrays]]
[[Day 76 - Plotly Charts]]
[[Day 75 - Google Trends Data Resampling]]
### Seaborn
Seaborn is a Python data visualization library based on [matplotlib](https://matplotlib.org/). It provides a high-level interface for drawing attractive and informative statistical graphics.
Basic Syntax
```Python
# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
```
#### syntax


## References
[Seaborn docs](https://seaborn.pydata.org/tutorial/introduction.html)
[Seaborn themes](https://python-graph-gallery.com/104-seaborn-themes/)
