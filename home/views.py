from django.shortcuts import render


# Create your views here.
def home(request):
    """Renders the index page"""
    return render(request, 'home.html')
