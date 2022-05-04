from django.contrib import admin
from .models import CaseType, State, District, Place

# Register your models here.
admin.site.register(CaseType)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Place)