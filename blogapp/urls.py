from django.urls import path

from blogapp.views import *

urlpatterns = [
    path('', PostView.as_view(), name='blog'),
    path('<int:pk>', SingleBlogView.as_view(), name='single-blog')
]
