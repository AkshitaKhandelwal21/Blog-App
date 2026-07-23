from django.contrib import admin
from .models import Blogs

# Register your models here.

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "id", "customize_title", "content", 
    ) 
    
    def customize_title(self, obj):
        if obj.title.islower():
            return obj.title.capitalize()
    
        return obj.title

    # @admin.display(ordering="content")
    # clicking column will sort by specified name
    def content_length(self, obj):
        return "Content"
    
    # makes the columns clickable
    list_display_links = (
    "customize_title",
)