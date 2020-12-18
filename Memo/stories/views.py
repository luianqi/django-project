from django.shortcuts import render
from .models import Info
from .forms import InfoForm

def endpage(request):
    story = Info.objects.order_by('-date')
    return render(request, 'main/endpage.html', {'story': story})


def create(request):
    form = InfoForm()

    data = {
        'form': form
    }
    return render(request, 'main/create.html', data)
   

   