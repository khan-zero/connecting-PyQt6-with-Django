from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MyDataView(APIView):
    def get(self, request):
        data = {"message": "Hello from Django!"}
        return Response(data, status=status.HTTP_200_OK)

