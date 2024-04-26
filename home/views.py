from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from home.models import *

from rest_framework import serializers
from home.serializer import *
from rest_framework.response import Response
# Create your views here.




@api_view(['delete'])

def infoview(request,id):
        user=info1.objects.filter(id=id)
        serializer=info1serializer(user,many=True)
        for data in serializer.data:
              data_serializer=infoserializer(data=data)
              if data_serializer.is_valid():
                     data_serializer.save()
              else:
                     return Response({'status':200,'message':'somthing is wrrong'})
        return Response({'status':200,'message':'success'})