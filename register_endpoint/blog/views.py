from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from register_endpoint.urls import *

def show_urls(urllist, depth=0):
    for entry in urllist:
        print "  " * depth, entry.regex.pattern
        if hasattr(entry, 'url_patterns'):
            show_urls(entry.url_patterns, depth + 1)

class Test(APIView):
    def get(self, request, *args, **kwargs):
        show_urls(urls.urlpatterns)
        return Response({'message': 'This is just a test'})
