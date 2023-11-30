"""
A feature under development for DuckDB is an API compatible with Apache Spark.
This will allow you to use the same code for both DuckDB and Apache Spark.

Many Spark workloads do not require the full power of a cluster or do not utilize the full power of a cluster.
It can be much more cost effective to run your workloads on a single machine using all cores and memory available.

DuckSpark allows us to reuse our Spark code on a single machine with DuckDB.
"""

import duckdb
import pandas as pd
from deltalake import DeltaTable

"""
Challenge 1:
Use the full iris dataset from the previous challenges.

Use the DuckSpark API to do the following:

Compute the average of the sepal_length, sepal_width, petal_length and petal_width per species.

Find the species that has the highest average petal_width.

- https://duckdb.org/docs/api/python/spark_api
- https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.mean.html
- https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.max.html

"""


"""
Challenge 2:

Find the species that has the highest average surface area of the petals.

The surface area of an ellipse is calculated as follows:
    
        pi * a * b
    
    where a and b are the lengths of the semi-major and semi-minor axes, 
    which is half the length (a) and half the width (b) of the petal.

Use withColumn to add a column to your table with the surface area of the petal.
- https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withColumn.html

"""
