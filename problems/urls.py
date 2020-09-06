from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('problem1/', views.problem1, name='problem1'),
    path('problem2/', views.problem2, name='problem2'),
    path('problem3/', views.problem3, name='problem3'),
    path('endpage/', views.endpage, name='endpage'),
    path('check/', views.check, name='check'),
    path('check2/', views.check2, name='check2'),
    path('check3/', views.check3, name='check3'),
]
