from django.contrib import admin
from .models import *
from home.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Cita)
admin.site.register(Estado)