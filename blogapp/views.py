from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator

from blogapp.models import Post


class PostView(ListView):
    model = Post
    template_name = 'blog.html'
    context_objects_name = ' posts'
    pagination_by = 2


class SingleBlogView(DetailView):
    model = Post
    template_name = 'single-blog.html'
    context_object_name = 'post'
