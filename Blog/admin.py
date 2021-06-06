from django.contrib import admin
from .models import Post, Comentario

from django.db import models
# Register your models here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','author', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'contenido']
    prepopulated_fields = {'slug': ('title',)}

    #def get_queryset(self, request):
    #    qs = super(PostAdmin, self).get_queryset(request)
    #    return qs.filter(author=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["initial"] = request.user.id
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
    has_class_permission = super(PostAdmin, self).has_change_permission(request, obj)

    if not has_class_permission:
        return False

    if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
        return False
        
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
