---
aliases:
  - dataframe selection
tags:
  - review
  - ml
References:
cssclasses:
j:
---
# dataframe selection
> [!NOTE] Intro: 
> Ways of selecting data in a pandas dataframe. 

- Each column can be referenced as: `df["NAME"]` where “NAME” is the column’s name. 
  With this method we would be getting all values for column A
- A slice can also be used to reference: `df[<slice>]`
  We would get an slice of the table in the rows space.
  > The slice `0:3` will output all rows from 0 to 3 and their properties (columns). 0 and 3 included 
- **df.loc[]**: This method selects based on two things: 
	- the row / rows
	- the columns
	  We choose some number of rows and some number of columns and the selection is done based on that. The way we choose can be either by referencing their names or an slice, a function…
	  If no rows or columns are selected it takes them all
```python
	df.loc[<somerows>, <somecoulmns>]	
```

- **df.iloc[]**: Works similar to the loc selection but it is all done with integers to identify each property | row. 

***
### Up
- [[1758564298-dataframe|dataframe]]
### Down
