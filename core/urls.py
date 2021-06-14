from django.urls import path
from .views import index


urlpatterns = [
    path('', index, name='index'),
    #path('cliente_novo/', cliente_novo, name='cliente_novo'),
]
