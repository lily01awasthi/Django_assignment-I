from django.contrib import admin
from .models import Blog,Author

# Register your models here.


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Blog)
class Blogs(admin.ModelAdmin):
    list_display = ('title','content','author','date_posted')