from django.shortcuts import render

# Create your views here.



def homepage(request):
    return render(request, 'index.html')

def porfolio_page(request):
    return render(request, 'portfolio-1.html')