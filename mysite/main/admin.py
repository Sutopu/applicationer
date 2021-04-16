from django.contrib import admin
from .models import Application, Level, Status, Role

admin.site.register(Application)
admin.site.register(Level)
admin.site.register(Status)
admin.site.register(Role)
# Register your models here.
