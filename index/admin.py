from django.contrib import admin

from index.models import Categories, Subcategory, Products, Reviews

# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount",]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "subcategory"]
    fields = [
        "name",
        "subcategory",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]

admin.site.register(Reviews)