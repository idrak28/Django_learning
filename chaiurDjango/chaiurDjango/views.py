from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("hello , idrak ")
    return  render(request,'index.html')
def about(request):
    return HttpResponse("hello , about ")

def contact(request):
    return HttpResponse("hello , contact ")

