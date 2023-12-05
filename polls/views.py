from django import HttpResponse


def index(request):
    return HttpResponse("Hello World! Welcomt to the polls index!")

# Create your views here.
