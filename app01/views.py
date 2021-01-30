from django.shortcuts import render,HttpResponse
from app01 import models

# Create your views here.
def add_book(request):
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list('tel')
    return HttpResponse(res)