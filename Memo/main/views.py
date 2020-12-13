from django.shortcuts import render


def frontpage(request):
    return render(request, 'main/frontpage.html')

def slider(request):
    return render(request, 'main/slider.html')