from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import clients
from .serializers import clients_serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Create your views here.
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def contact_Api(request):
    if request.method == 'POST':
        serializer = clients_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer._errors, status=400)
    elif request.method == 'GET':
        queryset = clients_serializer.objects.all()
        serializer_class = clients_serializer
        return JsonResponse(queryset, status=201)
    return JsonResponse(serializer_class._errors, status=400)


    
    
