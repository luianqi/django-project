from django.shortcuts import render
from .models import Info

def endpage(request):
    story = Info.objects.order_by('-date')
    return render(request, 'main/endpage.html', {'story': story})


