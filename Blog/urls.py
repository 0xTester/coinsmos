from django.urls import path
from . import views
from .views import PostListDest, PostDetail, CategoryView, contacto, busqueda,AuthorListView

urlpatterns = [
    path('', PostListDest.as_view(), name='blog-home'),
    path('categorias/<str:ctgs>/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('categorias/<str:ctgs>/', CategoryView, name = 'categoria'),
    path('contacto', contacto, name='pagina_contacto'),
    path('busqueda.html', busqueda, name = 'busqueda'),
    path('user/<str:username>/', AuthorListView.as_view(), name='user-posts'),

]
