from django.views.decorators.http import require_POST
from django.shortcuts import render, HttpResponse
from core.models import Embeddings


def index(request):
    """
    You can use this main function as a basis for your web app.
    Have it retrieve embeding data and render it in the html template for example!
    """
    return render(request, "index.html")


@require_POST
def upload_file(request):
    # Handle the uploaded file here
    uploaded_file = request.FILES['file']
    # Add your code to process the file

    # Return a response or redirect
    return render(request, "index.html")
