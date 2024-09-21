from django.shortcuts import render
from .models import Product, Review
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "render_string": "First page"
    }
    return render(request, template_name="myapp/index.html", context=context)