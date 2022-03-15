from django.urls import path
from .views import *

app_name = 'material'

urlpatterns = [
    path('', index, name='index'),
    path('material_form/', material_form, name='material_form'),
    path('<int:id>/',material_detail,name='material_detail')
]