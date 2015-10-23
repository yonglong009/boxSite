from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    html = "<html><body>NOW is: OK.</body></html>"
    return HttpResponse(html)
