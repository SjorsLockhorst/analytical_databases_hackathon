"""
Challenge 1:
Read both the csv file and the delta table into a duckdb database table.
Align the column names on the names provided:
    - sepal_length
    - sepal_width
    - petal_length
    - petal_width
    - species

Use a mix of the SQL and relational API to do the following:    
- https://duckdb.org/docs/api/python/dbapi
- https://duckdb.org/docs/api/python/relational_api

Merge the two tables with DuckDB SQL to get the complete iris dataset.

Query to find the species that has the highest average petal_width.

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
