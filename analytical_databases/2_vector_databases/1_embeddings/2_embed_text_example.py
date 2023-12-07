# %%
import re

import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity

from embetter.grab import ColumnGrabber
from embetter.text import SentenceEncoder

# This pipeline grabs the `text` column from a dataframe
# which then get fed into Sentence-Transformers' all-MiniLM-L6-v2.
text_emb_pipeline = make_pipeline(
    ColumnGrabber("text"), SentenceEncoder("all-MiniLM-L6-v2")
)

# dataf = pd.DataFrame({"text": ["positive sentiment", "super negative"]})
# X = text_emb_pipeline.fit_transform(dataf)
#
# print(X.shape)

"""
Challenge:
Load the /data/EWD_trip_report.txt into memory and split it into sentences. Generate embeddings for all sentences.
Select a sentence from the text and find the most similar sentences to it.

Try to find out what Edgar Wiebe Dijkstra said about the mistakes attributable to John von Neumann.

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

"""

# %%
with open("data/EWD_trip_report.txt", "r") as file:
    contents = file.read()

contents

# %%
clean_texts = re.sub(r"\n+", "", contents).strip().split(". ")
df = pd.DataFrame(clean_texts, columns=["text"])

# %%
embeddings = text_emb_pipeline.fit_transform(df)

# %%
embeddings

# %%
query_sent = pd.DataFrame(["John von Neumann"], columns=["text"])
query_embeddings = text_emb_pipeline.transform(query_sent)
query_embedding = query_embeddings

# %%
similarities = cosine_similarity(query_embedding, embeddings)

# %%
k = 5
similiar_indices = np.argsort(similarities)[0][-k:]
most_similiar_idx = similiar_indices[::-1]

for sim_text in df.iloc[most_similiar_idx]["text"]:
    print(sim_text)
    print()
