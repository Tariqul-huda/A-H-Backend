from django.shortcuts import render
from home.models import Category,Product
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q
def men(request):
    men = Product.objects.filter(category=1)
    data = men
    if not data:
        return
    json_data = serializers.serialize('json',data)
    return HttpResponse(json_data,content_type='application/json')






# Create your views here.
