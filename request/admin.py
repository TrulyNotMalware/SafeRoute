from django.contrib import admin
from .models import Request
# Register your models here.

class RequestAdmin(admin.ModelAdmin):
     pass

admin.site.register(Request, RequestAdmin)