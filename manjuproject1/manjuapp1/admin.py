from django.contrib import admin
from manjuapp1.models import Library

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Author', 'ISBN']
admin.site.register(Library, LibraryAdmin)