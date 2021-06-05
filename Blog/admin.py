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
        #qs = super(PostAdmin, self).get_queryset(request)
        #return qs.filter(author=request.user)
    def get_form(self, request, obj=None, **kwargs):

        form = super().get_form(request,obj,**kwargs)
        form.author = request.user
        return form
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
