from django.shortcuts import render,HttpResponse
from app01 import models

# Create your views here.
def add_book(request):
    books = models.Book.objects.values_list('id','title','price','publish','pub_date')
    print(books,type(books))
    return HttpResponse("<p>数据添加成功！</p>")