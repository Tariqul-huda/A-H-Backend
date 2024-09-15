from django.shortcuts import render
from .models import Category,Product
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q
def home(request):
    men = Product.objects.filter(category=1)[:1]
    women = Product.objects.filter(category=2)[:1]
    data = men | women
    if not data:
        return
    json_data = serializers.serialize('json',data)
    return HttpResponse(json_data,content_type='application/json')






# Create your views here.
