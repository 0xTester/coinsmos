from django.contrib import admin
from .models import Post, Comentario

from django.db import models
# Register your models here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class PostAdmin(admin.ModelAdmin, LoginRequiredMixin):
    list_display = ('title', 'slug', 'status','author', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'contenido']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['dispatch']
    #def get_queryset(self, request):
        #qs = super(PostAdmin, self).get_queryset(request)
        #return qs.filter(author=request.user)
    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        post = self.get_object()
        if not (post.author == user):
            raise PermissionDenied
        return handler
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
