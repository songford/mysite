from django.http import HttpResponse

def index(httpRequest):
    return HttpResponse("Hello world")
