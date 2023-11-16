"""
A feature under development for DuckDB is an API compatible with Apache Spark.
This will allow you to use the same code for both DuckDB and Apache Spark.

Many Spark workloads do not require the full power of a cluster or do not utilize the full power of a cluster.
It can be much more cost effective to run your workloads on a single machine using all cores and memory available.

DuckSpark allows us to reuse our Spark code on a single machine with DuckDB.

- https://duckdb.org/docs/api/python/spark_api

"""

import duckdb
import pandas as pd

"""
Challenge:
Use the full iris dataset from the previous challenges.

Use the DuckSpark API to do the following:

Compute the standard deviation of the sepal_length, sepal_width, petal_length and petal_width per species.



"""
