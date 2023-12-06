"""
read data from Delta Table with delta-rs and connect DuckDB then execute a query on it.

"""
import duckdb
from deltalake import DeltaTable

"""
Challenge 1:

Delta tables are columnar data structures. They are very efficient for analytical workloads.
They are a combination of parquet files and a transaction log see /workspace/data/iris_dataset_part_1.

Delta tables are a popular format for data lakes. They are also a popular format for data warehouses.
Here we want to perform analytical workloads on the data in the Delta table with DuckDB.
We bridge the gap between the two via Arrow. Arrow is a transfer format for columnar data that is an industry standard.
It allows DuckDB to use the data in the Delta table without having to copy it.

Steps:
- Load the deta table located at `/workspace/data/iris_dataset_part_1` with DeltaTable.
- Convert the DeltaTable to an Arrow dataset with `.to_pyarrow_dataset()` 
- Load the Arrow dataset into a duckdb with `duckdb.arrow()`

read the documentation for more information and support:
- https://delta-io.github.io/delta-rs/usage/querying-delta-tables/

"""


"""
DuckDB SQL is the main interface to DuckDB. It is a full SQL implementation that supports a wide variety of SQL features.

We create a connection to the DuckDB database with `con = duckdb.connect()` and we use `result = con.execute("SQL STATEMENT") to execute SQL statements.

The result is a Cursor object that can be used to fetch the results with `result.fetchone()` or `result.fetchall()`.
Alternatively we can use `result.df()` to convert the result to a Pandas DataFrame.

please read the documentation for more information:
- https://duckdb.org/docs/api/python/dbapi


Challenge 2:
Rename the columns of the duckdb table with the sql ALTER TABLE statement to the following:
    - sepal_length
    - sepal_width
    - petal_length
    - species

    
ALTER TABLE SQL statement for renaming a column in a table:
'ALTER TABLE <table_name> RENAME old_name TO new_name;'

ALTER TABLE documentation:
- https://duckdb.org/docs/sql/statements/alter_table

After renaming query the DuckDB table with SQL and compute the max sepal_width per species.
Print the results as a dataframe.

"""
