from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','modificado')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','modificado')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

