from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='station_index'),
    path('criminal_details/<int:cid>', criminal_details, name='station_criminal_details'),
    path('add_criminals/', add_criminals, name='station_add_criminals'),
    path('manage_criminals/', manage_criminals, name='station_manage_criminals'),
    path('remove_criminals/<int:cid>', remove_criminals, name='station_remove_criminals'),
    path('edit_criminals/<int:cid>', edit_criminals, name='station_edit_criminals'),
]