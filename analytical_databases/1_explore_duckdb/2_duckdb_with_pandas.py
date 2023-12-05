"""
Here we create a simple DuckDB database and execute a query on it.
The database is created in-memory, so no file is created.
The data is stored in a Pandas DataFrame based on a csv file in the "../data" directory.
"""
import duckdb
import pandas as pd

iris_2_pdf = pd.read_csv("/workspace/data/iris_dataset_part_2.csv")


"""
Challenge 1:

Rename the columns of the pandas dataframe to the following:
    - sepal_length
    - petal_length
    - petal_width
    - species

Query the Pandas dataframe with DuckDB and compute the max of the sum of petal_width and petal_length per species.
Print the results.

ref:
- https://duckdb.org/2021/05/14/sql-on-pandas.html
"""
