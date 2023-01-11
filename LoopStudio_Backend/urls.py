# from django.urls import path
# # from rest_framework.urlpatterns import format_suffix_patterns
# from  LoopStudio_Backend import views

# urlpatterns = [
#     path('', views.snippet_list),
  
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path, include
from LoopStudio_Backend import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.snippet_list),
    path('LoopStudio_Backend/<int:pk>/', views.snippet_detail),


]
urlpatterns = format_suffix_patterns(urlpatterns)