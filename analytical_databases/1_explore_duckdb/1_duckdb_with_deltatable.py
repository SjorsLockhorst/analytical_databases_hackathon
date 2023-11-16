"""
read data from Delta Table with delta-rs into DuckDB then execute a query on it.

"""
import duckdb
from deltalake import DeltaTable

dt = DeltaTable("/workspace/data/iris_dataset_part_1")
dataset = dt.to_pyarrow_dataset()
ex_data = duckdb.arrow(dataset)

print(ex_data.columns)

"""
Challenge:
Rename the columns of the duckdb table to the following:
    - sepal_length
    - sepal_width
    - petal_length
    - species
"""

result = ex_data.filter()
print(result.fetchall())
