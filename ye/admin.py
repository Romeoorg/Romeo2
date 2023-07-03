from django.contrib import admin
from .models import my_table,Review,Tag

# Register your models here.
admin.site.register(my_table)
admin.site.register(Review)
admin.site.register(Tag)