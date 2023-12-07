"""
`pgvector` is a PostgreSQL extension for efficient vector storage and computation. 
It is designed to work with high-dimensional vectors, such as those used in machine learning and data analysis. 
It provides functions for vector operations, such as similarity search, nearest neighbor search, and dot product calculation. 
It's particularly useful when working with large datasets where these operations would otherwise be computationally expensive.
"""
# %%
import os

import psycopg
from pgvector.psycopg import register_vector
from dotenv import load_dotenv

import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity

from embetter.grab import ColumnGrabber
from embetter.vision import ImageLoader, TimmEncoder

load_dotenv(".devcontainer/.env")

# %%
PASSWORD = os.getenv("POSTGRES_PASSWORD")
BASE_PSQL = f"postgresql://postgres:{PASSWORD}@localhost:15432"
VECTOR_PSQL = f"{BASE_PSQL}/vector"

# %%

EMBEDDING_LENGTH = 1280

conn = psycopg.connect(BASE_PSQL, autocommit=True)
conn.execute("DROP DATABASE IF EXISTS vector")
conn.execute("CREATE DATABASE vector")

with psycopg.connect(VECTOR_PSQL) as conn:
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS embeddings")
        cur.execute(
            f"CREATE TABLE embeddings (id int, embedding vector({EMBEDDING_LENGTH}))"
        )

# %%

"""
Challenge:

Insert the embeddings for the cat images into the `embeddings` table.
Make sure to set the correct vector length based on the model you used to generate the embeddings.

Then query the database to obtain the 5 most similar embeddings a cat image from /data/images/requested_pets.

# Query the database to obtain similar embeddings
# cur.execute('SELECT * FROM embeddings ORDER BY embedding <-> %s LIMIT 5', (embedding,))
# cur.fetchall()

"""


# %%

# This pipeline grabs the `img_path` column from a dataframe
# then it grabs the image paths and turns them into `PIL.Image` objects
# which then get fed into MobileNetv2 via TorchImageModels (timm).
image_emb_pipeline = make_pipeline(
    ColumnGrabber("img_path"),
    ImageLoader(convert="RGB"),
    TimmEncoder("mobilenetv2_120d"),
)



BASE_PATH = "data/images/cats_vs_dogs"
CAT_PATH = os.path.join(BASE_PATH, "cat")
DOG_PATH = os.path.join(BASE_PATH, "dog")

all_pics = []

for dog_pic in os.listdir(DOG_PATH):
    if dog_pic.endswith("jpg"):
        dog_path = os.path.join(DOG_PATH, dog_pic)
        all_pics.append(("dog", dog_path))

for dog_pic in os.listdir(CAT_PATH):
    if dog_pic.endswith("jpg"):
        dog_path = os.path.join(CAT_PATH, dog_pic)
        all_pics.append(("cat", dog_path))



all_animals_df = pd.DataFrame(all_pics, columns=["species", "img_path"])

# %%
cat_idx = (all_animals_df.species == "cat").to_numpy()
dog_idx = (all_animals_df.species == "dog").to_numpy()

# %%
embeds = image_emb_pipeline.fit_transform(all_animals_df)

# %%
dog_embeds = embeds[dog_idx]
cat_embeds = embeds[cat_idx]

# %%
# Connect to an existing database
with psycopg.connect(VECTOR_PSQL) as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Execute a command: this creates a new table
        register_vector(conn)


        for idx, embedding in enumerate(embeds):
            conn.execute(
                "INSERT INTO embeddings (id, embedding) VALUES (%s, %s)", (idx, embedding)
            )

        # Make the changes to the database persistent
        conn.commit()

# %%
new_animal = pd.DataFrame(
        [["cat", "data/images/cats_vs_dogs/requested_pets/4312.jpg"]],
        columns=["species", "img_path"]
)

embedding = image_emb_pipeline.transform(new_animal)[0]

# %% 
requested_embedding_list = embedding.tolist()
array_literal = str(requested_embedding_list)

# Connect to your database and execute the query
with psycopg.connect(VECTOR_PSQL) as conn:
    with conn.cursor() as cur:
        # Modify the query to handle a PostgreSQL array literal
        query = f"SELECT * FROM embeddings ORDER BY embedding <=> '{array_literal}' LIMIT 5;"
        # cur.execute('SELECT * FROM embeddings ORDER BY embedding <-> %s LIMIT 5', (embedding,))

        cur.execute(query)
        top_similar = cur.fetchall()

most_sim_cats = list(id for id, _ in top_similar)
most_sim_cats
