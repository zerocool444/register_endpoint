from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Testing(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': 'This is just a test'})
