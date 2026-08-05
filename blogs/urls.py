from django.urls import path, include

from blogs.views import *

urlpatterns = [
    # path('home/', views.home),
    # path('blog_list/', views.blog_list),
    # path('blog_detail/<int:id>', views.blog_detail),
    # path('blog_create/', views.blog_create),
    # path('blog_update/<int:id>', views.blog_update),
    # path('blog_delete/<int:id>', views.blog_delete),
    # path('my_blogs/', views.my_blogs),
    
    # path('', HomeView.as_view(), name='home'),
    # path('blogs/', BlogView.as_view(), name='blogs'),
    path('bloglist/', ListBlogView.as_view(), name='bloglist'),
    # path('blogdetail/<int:pk>', BlogDetailView.as_view(), name='blogdetail'),
    path('blogcreate/', CreateBlogView.as_view(), name='blogcreate'),
    
    
]