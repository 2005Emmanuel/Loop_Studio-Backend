from .models import clients
from rest_framework import serializers
class clients_serializer(serializers.ModelSerializer):
    model = clients
    fields = ['id', 'fullname', 'email', 'message']