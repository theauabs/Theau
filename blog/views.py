from django.shortcuts import render
from .models import Post02


# Create your views here.
def home(request):
    context = {
        'Posts': Post02.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

