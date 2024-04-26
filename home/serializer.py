from home.models import *
from home.views import *
from rest_framework import serializers



class infoserializer(serializers.ModelSerializer):
    class Meta:
        model=info
        fields="__all__"
        
    

class info1serializer(serializers.ModelSerializer):
    class Meta:
        model=info1
        fields='__all__'

   