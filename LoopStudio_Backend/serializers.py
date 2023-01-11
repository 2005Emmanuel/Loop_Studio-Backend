# from .models import clients
# from rest_framework import serializers
# class clients_serializer(serializers.ModelSerializer):
#     model = clients
#     fields = ['fullname', 'email', 'message']
from rest_framework import serializers
from LoopStudio_Backend.models import Snippet



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language']