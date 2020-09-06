from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/check/', views.check, name='check'),
    path('foul/', views.foul, name='foul'),
    path('<int:pk>/correct/', views.correct, name='correct'),
]