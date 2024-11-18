from django.urls import path 
from . import views

urlpatterns=[
    path('bv/',views.Basicdetails_API.as_view()),
    path('bv/<int:pk>/',views.Basicdetails_API.as_view())
]