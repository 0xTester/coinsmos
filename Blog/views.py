from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.

class AuthorListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        post_autor = Post.objects.filter(author=user).order_by('-created_on')
        return post_autor

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ultimas = Post.objects.filter(status=1).order_by('-created_on')[0:4]
        context_data['ultimas'] = ultimas
        return context_data

class PostListDest(ListView):

    model = Post
    template_name = 'Blog/index.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ultimas = Post.objects.filter(status=1).order_by('-created_on')
        paginator = Paginator(ultimas, self.paginate_by)
        page = self.request.GET.get('page')
        context_data['destacados'] = Post.objects.filter(status=1, destacado=1).order_by('-created_on')
        try:
            ultimas = paginator.page(page)
        except PageNotAnInteger:
            ultimas = paginator.page(1)
        except EmptyPage:
            ultimas = paginator.page(paginator.num_pages)
        context_data['ultimas_publicaciones'] = ultimas
        return context_data

class PostDetail(DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ultimas = Post.objects.filter(status=1).order_by('-created_on')[0:4]
        context_data['ultimas'] = ultimas
        return context_data

def CategoryView(request, ctgs):
    ctgs = ctgs.lower()
    post_ctgs = Post.objects.filter(categoria = ctgs)
    ultimas = Post.objects.filter(status=1).order_by('-created_on')[0:4]
    paginator = Paginator(post_ctgs, 6)
    page = request.GET.get('page')
    try:
        post_ctgs = paginator.page(page)
    except PageNotAnInteger:
        post_ctgs = paginator.page(1)
    except EmptyPage:
        post_ctgs = paginator.page(paginator.num_pages)
    return render(request, 'Blog/categorias.html', {'ctgs' : ctgs.title(), 'page':page ,'post_ctgs':post_ctgs,'ultimas':ultimas})

def contacto(request):
    return render(request, 'Blog/contacto.html')

def busqueda(request):
    query = request.GET.get('q', '')
    queryset_list = Post.objects.filter(status = 1).order_by('-created_on')
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list' : queryset,
        'title' : 'List',
        'page' : page,
    }
    return render(request, 'Blog/busqueda.html', context)
