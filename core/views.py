from django.shortcuts import render

from . import models 
# Create your views here.



def homepage(request):
    context = {
        'about': models.About.objects.get(id=1),
        'coding_skills': models.CodingSkill.objects.all(),
        'education': models.Education.objects.all().order_by("-id"),
        'experiences': models.Experience.objects.all().order_by("-id"),
        'portfolio': models.Portfolio.objects.all(),
    }
    return render(request, 'index.html', context=context)

def porfolio_page(request, id):
    context = {
        'portfolio': models.Portfolio.objects.get(id=id)
    }
    return render(request, 'portfolio.html', context=context)