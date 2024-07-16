from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def aboutme(request):
    return render(request, 'aboutme.html')
def contact(request):
    return render(request, 'contact.html')
def projects(request):
    return render(request, 'projects.html')