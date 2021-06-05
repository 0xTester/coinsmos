from django.contrib import admin
from .models import Post, Comentario
from django.core.exceptions import PermissionDenied
from django.db import models
# Register your models here.


class PostAdmin(admin.ModelAdmin,LoginRequiredMixin, edit.UpdateView):
    list_display = ('title', 'slug', 'status','author', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'contenido']
    prepopulated_fields = {'slug': ('title',)}

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        post = self.get_object()
        if not (post.author == user or user.is_superuser):
            raise PermissionDenied
        return handler

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
