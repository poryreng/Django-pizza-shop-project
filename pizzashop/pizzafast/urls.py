from django.urls import path, include
from .views import *
from .import views


urlpatterns = [
    path('', index, name="index"),
    path('createpizza',views.create_pizza, name='create_pizza'),
    path('deliverypayment',views.delivery, name='delivery'),
    path('done',views.success, name='success'),
]
