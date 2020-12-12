from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>check</h4>')

def about(request):
    return HttpResponse('<h4>FJk</h4>')