from django.shortcuts import render, redirect
from .models import Info
from .forms import InfoForm

def endpage(request):
    story = Info.objects.order_by('-date')
    return render(request, 'main/endpage.html', {'story': story})


def create(request):
    error = ''
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('endpage')
    else:
        form = InfoForm()

    data = {
        'form': form,
        'error': error
    }


    return render(request, 'main/create.html', data)
