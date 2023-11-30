"""
Here we create a simple DuckDB database and execute a query on it.
The database is created in-memory, so no file is created.
The data is stored in a Pandas DataFrame based on a csv file in the "../data" directory.
"""
import duckdb
import pandas as pd

iris_2_pdf = pd.read_csv("/workspace/data/iris_dataset_part_2.csv")

"""
Challenge:
Rename the columns of the pandas dataframe to the following:
    - sepal_length
    - petal_length
    - petal_width
    - species
"""

# Create a DuckDB database in-memory
con = duckdb.connect(database=":memory:", read_only=False)

# Load the data from a csv file into a Pandas DataFrame
result = duckdb.query("SELECT * FROM iris_2_pdf")


# Print the result
print(result.fetchall())
