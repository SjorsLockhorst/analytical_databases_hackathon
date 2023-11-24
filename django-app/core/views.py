from django.shortcuts import render, HttpResponse
from core.models import Embeddings


def index(request):
    """
    You can use this main function as a basis for your web app.
    Have it retrieve embeding data and render it in the html template for example!
    """
    return render(request, "index.html")
