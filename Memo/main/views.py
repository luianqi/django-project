from django.shortcuts import render


def layout(request):
    return render(request, 'main/layout.html')

def slider(request):
    return render(request, 'main/slider.html')

def endpage(request):
    return render(request, 'main/endpage.html')