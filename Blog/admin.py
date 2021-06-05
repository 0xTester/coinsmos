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
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs['choices'] = (
                ('accepted', 'Accepted'),
                ('denied', 'Denied'),
            )
            
        return super().formfield_for_choice_field(db_field, request, **kwargs)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
