from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator

from blogapp.models import Post


class PostView(TemplateView):
    model = Post
    template_name = 'blog.html'
    object_list = Post.objects.all()
    extra_context = {"object_list": object_list}
    pagination_by = 2


class SingleBlogView(DetailView):
    model = Post
    template_name = 'single-blog.html'
    context_object_name = 'post'
