"""
DuckDB can be used to access in-memory pandas dataframes.
The data is stored in a Pandas DataFrame based on a csv file in the "../data" directory.
"""
import duckdb
import pandas as pd

iris_2_pdf = pd.read_csv("data/iris_dataset_part_2.csv")

"""
Please read the README.md in this directory first.


DuckDB SQL is the main interface to DuckDB. It is a full SQL implementation that supports a wide variety of SQL features.
DuckDB can transparantly query Pandas DataFrames as they fully support Arrow.
Arrow is a transaction framework for columnar data that is an industry standard.

We can query with an SQL statement with duckdb.query("SQL query"). 
Within this SQL statement we can directly refer to any Pandas dataframe we have in memory.
We use the name of the Pandas Dataframe variable as the table name in the SQL statement.
For example "SELECT * from iris_2_pdf;" will select all rows from the Pandas dataframe defined above.

Please read the documentation for more information:

- transparant querying pandas: https://duckdb.org/2021/05/14/sql-on-pandas.html
- SQL API: https://duckdb.org/docs/api/python/dbapi

Challenge 1:

Rename the columns of the pandas dataframe, using df.rename(dict), to the following:
    - sepal_length
    - petal_length
    - petal_width
    - species

Query the Pandas dataframe with DuckDB SQL and compute the mean petal_width per species.
Print the results by moving it to a dataframe with duckdb.query("SQL query").to_df() .

ref:
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html
"""

new_columns = ["sepal_length", "petal_length", "petal_width", "species"]
mapper = {old_col: new_col for old_col,
          new_col in zip(iris_2_pdf.columns, new_columns)}
iris = iris_2_pdf.rename(columns=mapper)

mean_petal_width = duckdb.query("select MEAN(petal_width), species from iris group by species").to_df()
print(mean_petal_width)
