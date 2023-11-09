"""
Here we use an approach to creating embeddings with scikit-learn and the embetter library.

https://koaning.github.io/embetter/applications/#lite-embeddings

https://github.com/koaning/embetter

"""
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

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
