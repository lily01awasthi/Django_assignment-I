from django.shortcuts import render
from .models import Blog,Author


# Create your views here.

def home(req):
    context = {
        'name' : 'Lalita Awasthi'
    }
    return render(req,'index.html',context)

def blog(req):
    context = {
        'obj': Blog.objects.all()

    }
    return render(req,'blog.html',context)

