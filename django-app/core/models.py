# This is an auto-generated Django model module based on the vector database
from django.db import models
from pgvector.django import VectorField


class Embeddings(models.Model):
    id = models.IntegerField(blank=True, null=True)
    # TODO: Determine the correct amount of dimensions
    embedding = models.VectorField(dimensions=3)

    class Meta:
        managed = False
        db_table = "embeddings"
