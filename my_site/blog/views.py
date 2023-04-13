from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def starting_page(request):
    return HttpResponse("Home page")


def posts(requst):
    return HttpResponse("Posts page")


def posts_detail(request):
    return HttpResponse("Posts detail page")
