from django.shortcuts import render

from . import models 
# Create your views here.



def homepage(request):
    context = {
        'about': models.About.objects.get(id=1)
    }
    return render(request, 'index.html', context=context)

def porfolio_page(request):
    return render(request, 'portfolio-1.html')