from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detailed/<str:slug>',views.detailed, name='detailed'),
]
