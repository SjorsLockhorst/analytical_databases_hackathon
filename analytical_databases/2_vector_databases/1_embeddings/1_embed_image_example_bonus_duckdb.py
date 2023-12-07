"""
Please read the README.md in this directory first.

Here we use an approach to creating embeddings with scikit-learn and the embetter library.

https://koaning.github.io/embetter/applications/#lite-embeddings

https://github.com/koaning/embetter

"""
# %%
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity

from embetter.grab import ColumnGrabber
from embetter.vision import ImageLoader, TimmEncoder

# This pipeline grabs the `img_path` column from a dataframe
# then it grabs the image paths and turns them into `PIL.Image` objects
# which then get fed into MobileNetv2 via TorchImageModels (timm).
image_emb_pipeline = make_pipeline(
    ColumnGrabber("img_path"),
    ImageLoader(convert="RGB"),
    TimmEncoder("mobilenetv2_120d"),
)

dataf = pd.DataFrame({"img_path": ["data/images/cats_vs_dogs/cat/0.jpg"]})
X = image_emb_pipeline.fit_transform(dataf)
print(X.shape)

# %%


"""
Challenge 1:
Generate two numpy arrays with embeddings for the cats and dogs images respectively.

Then calculate the average cosine similarity within and between the cats and dogs embeddings.

Are cats more similar to cats than dogs are to dogs? and how similar are cats to dogs?

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

"""
# %%
import os

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
within_dog_sims = cosine_similarity(dog_embeds)
within_cat_sims = cosine_similarity(cat_embeds)
dog_vs_cat_sim = cosine_similarity(dog_embeds, cat_embeds)

# %%
print("Dogs within")
print(within_dog_sims.mean())
print("Cats within")
print(within_cat_sims.mean())
print("Dogs vs cats")
print(dog_vs_cat_sim.mean())

# %%



"""
Bonus Challenge:

For this challenge we need to go on the cutting edge and install DuckDB straight from the source.
For this we use `pip isntall --upgrade --pre duckdb`.
- https://github.com/duckdb/duckdb

The dev build has the array type of a fixed length. This is ideal to store numpy arrays of embeddings.
This is a very recent addition to DuckDB and it greatly speeds up multi-dimensional operations.
The Array type makes DuckDB suitable as an in-memory vector database.

- https://duckdb.org/docs/sql/data_types/array.html

All functions that support lists also support arrays. In addition, arrays specific functions are available.
Array specific functions are much more efficient as they can assume the fixed length of the array.
You can see that specific vector comparison functions are available, such as cosine_similarity.

- https://duckdb.org/docs/sql/data_types/array.html#functions

Challenge 2:

Create a table in DuckDB with two columns, image name and image embedding.
    
Then insert the cats and dogs embeddings into the table.
    
Then use the cosine_similarity function to find the most similar cat and dog images based on an example image from /workspace/data/images/requested_pets.

"""
