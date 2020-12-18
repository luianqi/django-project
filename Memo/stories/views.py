from django.shortcuts import render
from .models import Info

def endpage(request):
    story = Info.objects.order_by('-date')
    return render(request, 'main/endpage.html', {'story': story})


def create(request):
    return render(request, 'main/create.html')

# def create(request):
#     form = InfoForm()

#     data = {
#         'form': form
#     }
#     return render(request, 'main.create', data)