from django.shortcuts import render
from home.models import Category,Product
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q


def category(request):
    data = Product.objects.all()
    if not data:
        return
    json_data = serializers.serialize('json',data)
    return HttpResponse(json_data,content_type='application/json')

