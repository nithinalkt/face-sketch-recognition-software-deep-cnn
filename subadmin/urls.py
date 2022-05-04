from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='subadmin_index'),
    path('add_police_station/', add_police_station, name='subadmin_add_police_station'),
    path('get_city/', get_city, name='subadmin_get_city'),
    path('add_criminals/', add_criminals, name='subadmin_add_criminals'),
    path('criminal_details/<int:cid>', criminal_details, name='subadmin_criminal_details'),
    path('search_image/', search_image, name='subadmin_search_image'),
    path('manage_station/', manage_station, name='subadmin_manage_station'),
    path('remove_station/<int:s_id>', remove_station, name='subadmin_remove_station'),
    path('manage_criminals/', manage_criminals, name='subadmin_manage_criminals'),
    path('remove_criminals/<int:cid>', remove_criminals, name='subadmin_remove_criminals'),
    path('edit_criminals/<int:cid>', edit_criminals, name='subadmin_edit_criminals'),
]