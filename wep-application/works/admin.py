from django.contrib import admin

from works.models import Filter, Catalog, Category, Style, Work


class FilterAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'filter', 'text')


# class StyleAdmin(admin.ModelAdmin):
#     pass


class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'filter', 'category', 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Filter, FilterAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Style)
admin.site.register(Work, WorkAdmin)
