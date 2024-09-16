from django.contrib import admin

from blog.models import Blog, BlogComment

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(BlogComment)
