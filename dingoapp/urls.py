# import menu as menu
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("about/", AboutView.as_view(), name='about'),
    path("chefs/", ChefsView.as_view(), name='chefs'),
    path("food/", MenuView.as_view(), name='menu'),
    path("blog/", BlogView.as_view(), name='blog'),
    path("contact/", ContactView.as_view(), name='contact'),
    path("single-blog/", SingleView.as_view(), name='single'),
    path("elements/", ElementsView.as_view(), name='elements'),
    path("login/", login_user, name='login'),
    path("logout/", logout_user, name='logout'),

]
