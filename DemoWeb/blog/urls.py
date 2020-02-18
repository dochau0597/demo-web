from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('/lienhe', views.lienhe, name='lienhe'),    
    path('/login', views.login, name='login'),    
]