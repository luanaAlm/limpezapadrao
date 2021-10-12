from django.urls import path
from .views import PolitPriv, index, cliente_novo


urlpatterns = [
    path('', index, name='index'),
    path('cliente_novo/', cliente_novo, name='cliente_novo'),
    path('politPriv/', PolitPriv, name='politPriv'),

]
