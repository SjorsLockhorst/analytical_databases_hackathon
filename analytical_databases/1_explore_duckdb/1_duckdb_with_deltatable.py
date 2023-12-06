"""
read data from Delta Table with delta-rs into DuckDB then execute a query on it.

"""
import duckdb
from deltalake import DeltaTable

"""
Challenge 1:
- Load the deta table located at `/workspace/data/iris_dataset_part_1` with DeltaTable.
- Convert the DeltaTable to an Arrow dataset
- Load the Arrow dataset into a duckdb table

ref:
- https://delta-io.github.io/delta-rs/usage/querying-delta-tables/

"""


"""
Challenge 2:
Rename the columns of the duckdb table to the following:
    - sepal_length
    - sepal_width
    - petal_length
    - species

Query the DuckDB table with SQL and compute the max sepal_width per species.
Print the results.


ref:
- https://duckdb.org/docs/sql/statements/alter_table
"""
