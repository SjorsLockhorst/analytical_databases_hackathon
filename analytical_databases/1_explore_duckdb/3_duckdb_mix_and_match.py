"""
Challenge:
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

Merge the two tables into one table to get the complete iris dataset.

Then compute the average sepal_length, sepal_width, petal_length and petal_width per species.

Find the species that has the highest average petal_width.

"""
