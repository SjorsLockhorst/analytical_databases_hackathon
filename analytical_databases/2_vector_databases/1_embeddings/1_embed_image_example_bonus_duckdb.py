"""
Here we use an approach to creating embeddings with scikit-learn and the embetter library.

https://koaning.github.io/embetter/applications/#lite-embeddings

https://github.com/koaning/embetter

"""
import pandas as pd
from sklearn.pipeline import make_pipeline

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

dataf = pd.DataFrame({"img_path": ["/workspace/data/images/cats_vs_dogs/cat/0.jpg"]})
X = image_emb_pipeline.fit_transform(dataf)
print(X.shape)


"""
Challenge 1:
Generate two numpy arrays with embeddings for the cats and dogs images respectively.

Then calculate the average cosine similarity within and between the cats and dogs embeddings.

Are cats more similar to cats than dogs are to dogs? and how similar are cats to dogs?

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

"""


"""
Bonus Challenge:

For this challenge we need to go on the cutting edge and install DuckDB straight from the source.
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
