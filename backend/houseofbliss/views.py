from django.http import HttpResponse
from django.conf import settings
from pathlib import Path


def index(request):
    try:
        filepath = Path(settings.BASE_DIR.parent / 'frontend' /
                        'build' / 'index.html')
        with open(filepath, 'r') as file:
            return HttpResponse(file.read(), content_type='text/html')
    except FileNotFoundError:
        error_message = ("index.html file was not found in "
                         "the build directory.")
        return HttpResponse(error_message,
                            content_type='text/plain',
                            status=500)
