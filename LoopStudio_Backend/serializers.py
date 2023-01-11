# from .models import clients
# from rest_framework import serializers
# class clients_serializer(serializers.ModelSerializer):
#     model = clients
#     fields = ['fullname', 'email', 'message']
from rest_framework import serializers
from LoopStudio_Backend.models import Clients



class Clients_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'fullname', 'email', 'message']