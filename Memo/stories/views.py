from django.shortcuts import render

def endpage(request):
    return render(request, 'main/endpage.html')
