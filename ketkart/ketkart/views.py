from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from app.models import category

def Master(request):
    return render(request,'master.html')

def Index(request):
    Category = category.objects.all()
    context = {
        'category':category
    }
    return render(request,'index.html',context)