from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField



class Post(models.Model):
    STATUS = (
        (0, "Borrador"),
        (1, "Publicacion")
    )

    postd = (
        (0, "Estandar"),
        (1, "Destacado"),
    )

    categorias = (
        ('defi','Defi'),
        ('trading','Trading'),
        ('noticias','Noticias'),
        ('blockchain', 'Blockchain'),
        ('educacion','Educacion'),

    )


    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    categoria = models.CharField(max_length = 20, choices = categorias, default = 'Noticias')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    updated_on = models.DateTimeField(auto_now = True)
    thumbnail = models.ImageField(upload_to='thumbail_pics')
    content = RichTextUploadingField(config_name="custom_ckeditor", null = True)
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices = STATUS, default = 0)
    destacado = models.IntegerField(choices = postd, default = 0 )
    banner = models.ImageField(upload_to='banner_pics', blank=True)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
