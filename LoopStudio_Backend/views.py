# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# # from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# # from .models import clients
# from .serializers import clients_serializer
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# # Create your views here.
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Contact
# from .serializers import ContactSerializer

# class ContactViewSet(viewsets.ModelViewSet):
#     # queryset = clients.objects.create()
#     serializer_class = clients_serializer

# # @api_view(['POST'])
# def create(self, request, *args, **kwargs):
#      if request.method == 'POST':
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         # serializer.is_valid(raise_exception=True)
#         # self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# class ContactViewSet(viewsets.ModelViewSet):
#     # queryset = clients.objects.create()
#     serializer_class = clients_serializer
# @api_view(['POST',])
# @permission_classes((permissions.AllowAny,))
# def contact_Api(request):
#     if request.method == 'POST':
#         serializer = clients_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer._errors, status=400)

# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def contact_Api(request):
#     if request.method == 'POST':
#         serializer = clients_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from .models import Todo
# from .serializers import TodoSerializer

# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = clients.objects.all()
#         serializer = clients_serializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = clients_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response    
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from LoopStudio_Backend.models import Clients
from .serializers import Clients_Serializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def Contact_us_Api(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Clients.objects.all()
        serializer = Clients_Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Clients_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = Clients_Serializer(snippets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


  
