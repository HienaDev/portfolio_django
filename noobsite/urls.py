# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('soma/<int:a>/<int:b>', views.soma),
    path('bom_dia/', views.bom_dia),
    path('wow/', views.wow),
]