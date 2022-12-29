from django.contrib import admin
from .models import Newpost
# Register your models here.

class NewpostAdmin(admin.ModelAdmin):
    list_display=["Title","Description","Image"]


admin.site.register(Newpost,NewpostAdmin)