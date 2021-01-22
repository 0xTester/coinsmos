from django.contrib import admin
from .models import Post, Categoria, Comentario

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','author', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'contenido']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)
admin.site.register(Comentario)
