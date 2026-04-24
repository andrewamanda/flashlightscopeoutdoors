from django.contrib import admin

from dinette import models

admin.site.register(models.SuperCategory)
admin.site.register(models.Ftopics)
admin.site.register(models.Reply)
admin.site.register(models.DinetteUserProfile)
admin.site.register(models.SiteConfig)
admin.site.register(models.NavLink)


class CategoryAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'super_category',)
    list_display_links = ('name',)
    list_filter = ('super_category',)

    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description']
    exclude = []
    
    # sets up slug to be generated from brand name
    prepopulated_fields = {'slug' : ('name',)}
    
admin.site.register(models.Category, CategoryAdmin)




