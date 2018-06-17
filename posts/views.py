from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView

from posts.form import PostForm
from posts.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'posts/list.html'
    paginate_by = 7

    def get_queryset(self):
        result = super().get_queryset()
        return result.filter(status=Post.APPROVED).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wordplease'
        context['claim'] = 'Una plataforma de anuncios hecha con Django'
        return context


class BlogView(ListView):
    model = User
    template_name = 'posts/blogs.html'

    def get_queryset(self):
        result = super().get_queryset().filter(is_superuser=False)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blogs'
        context['claim'] = 'Una plataforma de anuncios hecha con Django'
        return context


class BlogDetailView(ListView):
    model = Post
    template_name = 'posts/blog-list.html'
    paginate_by = 7

    def get_queryset(self):
        user = User.objects.select_related().get(username=self.kwargs['username'])
        pk = user.pk
        result = super().get_queryset()
        return result.filter(owner=pk, status=Post.APPROVED).order_by('-created_on')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wordplease'
        context['claim'] = 'Una plataforma de post hecha con Django'
        return context


@method_decorator(login_required, name='dispatch')
class PostFormView(View):

    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/form.html', context)

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_ad = form.save()
            form = PostForm()
            messages.success(request, 'Anuncio creado correctamente')

        context = {'form': form}
        return render(request, 'posts/form.html', context)