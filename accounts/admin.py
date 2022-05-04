from django.contrib import admin
from .models import CaseType, State, District, Place, Officer, Station, User

# Register your models here.
admin.site.register(User)
admin.site.register(CaseType)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Place)
admin.site.register(Officer)
admin.site.register(Station)

