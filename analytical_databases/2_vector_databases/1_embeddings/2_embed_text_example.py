import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

from embetter.grab import ColumnGrabber
from embetter.text import SentenceEncoder

# This pipeline grabs the `text` column from a dataframe
# which then get fed into Sentence-Transformers' all-MiniLM-L6-v2.
text_emb_pipeline = make_pipeline(
    ColumnGrabber("text"), SentenceEncoder("all-MiniLM-L6-v2")
)

dataf = pd.DataFrame({"text": ["positive sentiment", "super negative"]})
X = text_emb_pipeline.fit_transform(dataf)

print(X.shape)

"""
Challenge:

Download 

"""
