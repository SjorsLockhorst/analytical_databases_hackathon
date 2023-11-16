"""
`pgvector` is a PostgreSQL extension for efficient vector storage and computation. 
It is designed to work with high-dimensional vectors, such as those used in machine learning and data analysis. 
It provides functions for vector operations, such as similarity search, nearest neighbor search, and dot product calculation. 
It's particularly useful when working with large datasets where these operations would otherwise be computationally expensive.
"""
import numpy as np
import psycopg
from pgvector.psycopg import register_vector


EMBEDDING_LENGTH = 3

conn = psycopg.connect("postgresql://postgres:hack@localhost:5432", autocommit=True)
conn.execute("DROP DATABASE IF EXISTS vector")
conn.execute("CREATE DATABASE vector")

with psycopg.connect("postgresql://postgres:hack@localhost:5432/vector") as conn:
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS embeddings")
        cur.execute(
            f"CREATE TABLE embeddings (id int, embedding vector({EMBEDDING_LENGTH}))"
        )


# Connect to an existing database
with psycopg.connect("postgresql://postgres:hack@localhost:5432/vector") as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Execute a command: this creates a new table

        register_vector(conn)

        embedding = np.array([1, 2, 3])

        conn.execute(
            "INSERT INTO embeddings (id, embedding) VALUES (%s, %s)", (1, embedding)
        )

        # Make the changes to the database persistent
        conn.commit()


"""
Challenge:

Insert the embeddings for the cat images into the `embeddings` table.
Make sure to set the correct vector length based on the model you used to generate the embeddings.

Then query the database to obtain the 5 most similar embeddings a cat image from /data/images/requested_pets.

# Query the database to obtain similar embeddings
# cur.execute('SELECT * FROM embeddings ORDER BY embedding <-> %s LIMIT 5', (embedding,))
# cur.fetchall()

"""
