from django.shortcuts import render
from django.http import HttpResponse

import json
from . import models, forms
# Create your views here.



def homepage(request):
    form = forms.ContactForm()
    context = {
        'about': models.About.objects.get(id=1),
        'coding_skills': models.CodingSkill.objects.all(),
        'cv': models.CV.objects.filter(id=1).first(),
        'education': models.Education.objects.all().order_by("-id"),
        'experiences': models.Experience.objects.all().order_by("-id"),
        'form': form,
        'portfolio': models.Portfolio.objects.all(),
        'social': models.Social.objects.filter(id=1).first(),
    }
    return render(request, 'index.html', context=context)

def porfolio_page(request, id):
    context = {
        'portfolio': models.Portfolio.objects.get(id=id)
    }
    return render(request, 'portfolio.html', context=context)

def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            message = {
                "type": "Success",
                "message": "Message received"
            }
            return HttpResponse(json.dumps(message), content_type="application/json", status="200")
        else:
            message = {
                "type": "Failure",
                "message": form.errors.as_text(),
            }
            return HttpResponse(json.dumps(message), content_type="application/json", status="200")