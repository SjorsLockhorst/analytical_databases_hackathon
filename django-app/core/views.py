from django.shortcuts import render, HttpResponse
from core.models import Embeddings


def index(request):
    return HttpResponse("Hello, world!")
