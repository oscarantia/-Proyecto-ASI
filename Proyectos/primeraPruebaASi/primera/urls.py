from django.urls import path 
from primera import views

urlpatterns=[
    path('',views.index, name='index'),
    path('postdieta',views.dietas_alimentacion.dieta, name='dieta'),
]

