from django.urls import path
from .views import *

urlpatterns = [
    path('', loginview, name='accounts_login'),
    path('logout/', logout_view, name='accounts_logout'),
]