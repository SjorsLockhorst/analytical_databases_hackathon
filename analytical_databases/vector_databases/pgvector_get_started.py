"""
Vector databases are becoming very popular in AI applications, but have been used in other fields as well.
They are used to store and query vectors, which are a type of data structure that can be used to represent many things.
For example, vectors can be used to represent images, text, audio, and video.

Querying is based on similarity search, which is a type of search that finds similar items in a database.
This is useful for many applications, such as finding similar images, text, audio, and video.

There are production ready solutions such as Milvus, that we might explore if time permits.

Here we use an extension for Postgres to handle vector similarity searches.
This is a great way to add this functionality in existing applications such as Django.

source:
* https://pypi.org/project/pgvector/
* https://github.com/pgvector/pgvector-python

"""
"""
`pgvector` is a PostgreSQL extension for efficient vector storage and computation. 
It is designed to work with high-dimensional vectors, such as those used in machine learning and data analysis. 
It provides functions for vector operations, such as similarity search, nearest neighbor search, and dot product calculation. 
It's particularly useful when working with large datasets where these operations would otherwise be computationally expensive.
"""

