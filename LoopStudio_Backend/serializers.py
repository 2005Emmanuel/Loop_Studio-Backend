from .models import clients
from rest_framework import serializers
class clients_serializer(serializers.ModelSerializer):
    model = clients
    fields = ['fullname', 'email', 'message']