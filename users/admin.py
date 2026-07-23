from django.contrib import admin
from .models import Users

# Register your models here.
admin.site.register(Users)

@admin.display(boolean=True)
def active(self, obj):
    return obj.is_active