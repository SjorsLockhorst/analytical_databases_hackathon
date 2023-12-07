# This is an auto-generated Django model module based on the vector database
from django.db import models
from pgvector.django import VectorField


class Embeddings(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    # TODO: Determine the correct amount of dimensions
    source_img = models.CharField()
    embedding = VectorField(dimensions=1280)

    class Meta:
        managed = False
        db_table = "embeddings"
