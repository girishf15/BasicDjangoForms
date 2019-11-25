from django.urls import path

from .views import *

urlpatterns = [
    path('', registerform, name='registration1'),
]
