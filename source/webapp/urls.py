from django.urls import path

from webapp.calculator import calculator
from webapp.views import index

urlpatterns = [
    path('add/', calculator, name='add'),
    path('subtract/', calculator, name='subtract'),
    path('multiply/', calculator, name='multiply'),
    path('divide/', calculator, name='divide'),
    path('', index)
]
