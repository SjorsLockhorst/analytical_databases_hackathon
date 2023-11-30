# Introduction to FindYourNewPet
You are visiting an asylum for discarded pets. You have picture from the internet of your favorite pet, and you want to find a similar pet in the asylum. You ask the asylum keeper if they have a pet that looks like the one in the picture. The asylum keeper says maybe, but they have so many pets that they can't remember them all. You ask if they have a database of pets, and they say yes. You ask if you can search the database for a pet that looks like the one in the picture. He says he is not sure, but provides you access to pictures of all pets.

## Goal
The goal is to find your perfect pet among the pictures of dogs and cats. We need to create embeddings for all the pictures and put them in a vector database. Then we use the picture of our favorite pet to search the vector database for similar pets. To help future visitors, we also create a web application that allows them to search for pets with Django.

## Data
The pictures of all the pets are found in /data/images/cat and /data/images/dog. Pick a favorite pet from /data/images/requested_pets. The pictures are from https://huggingface.co/datasets/cats_vs_dogs. Full image set can be downloaded here: https://www.microsoft.com/en-us/download/details.aspx?id=54765 

## Django
A Django app skeleton is provided in `/workspace/django-app`. It is your goal to write database models using PGVector (see provided example) and create a view that allows users to search for pets.
Users should be able to upload a picture of their preferred pet (https://djangocentral.com/uploading-images-with-django/). The view should return the top 10 most similar pets.

PGVector has django integration https://pypi.org/project/pgvector/#django use it to create models that include vector embeddings along standard database fields (see example model) such pet type (cat or dog) and Pet name.