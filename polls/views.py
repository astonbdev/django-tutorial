from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World! Welcome to the polls index!")


def number(request, number, **kwargs):
    breakpoint()
    return HttpResponse(
        f"This is the number route where you picked the number {number}"
    )

# Create your views here.
