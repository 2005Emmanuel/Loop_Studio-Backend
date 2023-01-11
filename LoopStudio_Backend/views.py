from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import clients
from .serializers import clients_serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
# from .models import Contact
# from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = clients.objects.all()
    serializer_class = clients_serializer

@api_view(['POST'])
def create(self, request, *args, **kwargs):
     if request.method == 'POST':
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def contact_Api(request):
#     if request.method == 'POST':
#         serializer = clients_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer._errors, status=400)


    
    
