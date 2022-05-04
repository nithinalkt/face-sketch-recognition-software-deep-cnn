from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='admin_dashboard'),
    path('add_case_type/', add_case_type, name='add_case_type'),
    path('remove_case_type/<int:case_type_id>', remove_case_type, name='remove_case_type'),
    path('add_sub_admin/', add_sub_admin, name='add_sub_admin'),
    path('manage_sub_admins/', manage_sub_admins, name='manage_sub_admins'),
    path('remove_sub_admin/<int:sub_id>', remove_sub_admin, name='remove_sub_admin'),
]