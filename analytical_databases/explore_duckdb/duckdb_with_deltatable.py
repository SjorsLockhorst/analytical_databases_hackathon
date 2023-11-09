"""
read data from Delta Table with delta-rs into DuckDB then execute a query on it.

"""
import duckdb
import pandas as pd

from deltalake import DeltaTable, write_deltalake

# df = pd.DataFrame({"x": [1, 2, 3]})
# write_deltalake("./data/delta_df", df)


dt = DeltaTable("/workspace/data/delta_df")
dataset = dt.to_pyarrow_dataset()
ex_data = duckdb.arrow(dataset)

result = ex_data.filter("x > 1")
print(result.fetchall())
