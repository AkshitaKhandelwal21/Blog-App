from django import views
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *

from blogs.forms import BlogForm
from blogs.models import Blogs


class CreateBlogView(CreateView):
    model = Blogs
    form_class = BlogForm
    template_name = "create_blog.html"
    
    
class ListBlogView(ListView):
    model = Blogs
    template_name = "blogs.html"
    context_object_name = 'blogs'
    paginate_by = 10
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['content'] = self.objects.all()