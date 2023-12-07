import math

import duckdb
from duckdb.typing import DOUBLE
import pandas as pd
from deltalake import DeltaTable

conn = duckdb.connect()

"""
Challenge 1:

Copy your code from the previous sections to do the following:
Read both the csv file and the delta table into a duckdb database table.
Align the column names on the names provided:
    - sepal_length
    - sepal_width
    - petal_length
    - petal_width
    - species



Join the two tables with a Left join on sepal_length, petal_length and species with DuckDB SQL to get the complete iris dataset.
Are the results of the join unique?
- https://duckdb.org/docs/sql/query_syntax/from#joins


Query the joined table to find the species that has the highest mean sum of sepal_width and petal_width.
- groupby species: https://duckdb.org/docs/sql/query_syntax/groupby
- sum and max: https://duckdb.org/docs/sql/aggregates

"""


"""
Challenge 2:
DuckDB User-Defined Functions (UDFs) allow us to extend the functionality of DuckDB with custom Python code.
These UDFs benefits from DuckDB’s fast execution model, SQL and data safety.

- https://duckdb.org/2023/07/07/python-udf.html
- https://duckdb.org/docs/api/python/function.html

After registring a Python function with DuckDB create_function it can be used in SQL queries.

Use a Python UDF to compute the surface area of the iris petals approximating each petal as an ellipse.
The surface area of an ellipse is calculated as follows:
        
            pi * a * b
        
        where a and b are the lengths of the semi-major and semi-minor axes, 
        which is half the length (a) and half the width (b) of the petal.

Find the species with the highest average petal surface area.

"""

# %%
iris_2_pdf = pd.read_csv("data/iris_dataset_part_2.csv")

new_columns = ["sepal_length", "petal_length", "petal_width", "species"]
mapper = {old_col: new_col for old_col,
          new_col in zip(iris_2_pdf.columns, new_columns)}

iris_df = iris_2_pdf.rename(columns=mapper)
duckdb.query("CREATE TABLE iris_df as SELECT * FROM iris_df")


# %%
# Load Delta Table and convert to Arrow dataset
dt = DeltaTable("data/iris_dataset_part_1/")
iris_py_arrow = dt.to_pyarrow_dataset()
duckdb.query("CREATE TABLE iris_pyarrow as SELECT * from iris_py_arrow")

# %%
# Renaming columns
new_columns = ["sepal_length", "sepal_width", "petal_length", "species"]
for old_name, new_name in zip(iris_py_arrow.schema.names, new_columns):
    duckdb.query(
        f"ALTER TABLE iris_pyarrow RENAME COLUMN '{old_name}' TO '{new_name}'")

# %%
length_pyarrow = len(duckdb.query("select * from iris_pyarrow").df())
length_pandas = len(duckdb.query("select * from iris_df").df())
expected_len = length_pyarrow + length_pandas

# %%
all_joined = duckdb.query("""
    SELECT * FROM iris_pyarrow 
    LEFT JOIN iris_df
        ON (
            iris_pyarrow.sepal_length = iris_df.sepal_length AND 
            iris_pyarrow.petal_length = iris_df.petal_length AND 
            iris_pyarrow.species = iris_df.species
        );
"""
)

all_distinct = duckdb.query("""
    SELECT DISTINCT(*) FROM iris_pyarrow 
    LEFT JOIN iris_df
        ON (
            iris_pyarrow.sepal_length = iris_df.sepal_length AND 
            iris_pyarrow.petal_length = iris_df.petal_length AND 
            iris_pyarrow.species = iris_df.species
        );
"""
)

# %%
res = duckdb.query("""
    SELECT species, sum_of_means
    FROM (
        SELECT 
            MEAN(petal_width + sepal_width) AS sum_of_means, 
            species 
        FROM all_joined 
        GROUP BY species
    )
    ORDER BY sum_of_means DESC
    LIMIT 1;
""")
print("Challenge 1.")
print(res)

# %%

def calc_surface_area(a, b):
    return math.pi * a * b

duckdb.create_function("calc_surface", calc_surface_area, [DOUBLE, DOUBLE], DOUBLE)

# %%
# Execute the query using the DuckDB connection
result_df = duckdb.query(
"""
SELECT species, MEAN(surface_area) as avg_surface
FROM (
    SELECT species, calc_surface(petal_length / 2, petal_width / 2) AS surface_area 
    FROM all_joined
)
GROUP BY species
ORDER BY avg_surface
DESC
LIMIT 1;
"""
)
print("Challenge 2.")
print(result_df)
