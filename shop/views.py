from django.shortcuts import render
from .models import Category, Product
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()[:8]
    }
    return render(request, 'shop/index.html', context=context)
