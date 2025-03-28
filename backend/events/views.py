from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
def show_all(request):
    return

@api_view(['PUT'])
def edit(request):
    return

@api_view(['POST'])
def create(request):
    return

@api_view(['DELETE'])
def delete(request):
    return

@api_view(['GET'])
def show_event(request):
    return

@api_view(['GET'])
def callback(request):
    return







