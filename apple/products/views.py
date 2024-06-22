from django.http import HttpResponse

def index(request):
    return HttpResponse("Products Page")

# Create your views here.
