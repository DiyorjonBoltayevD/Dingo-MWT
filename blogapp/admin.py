from django.contrib import admin

from blogapp.models import Post, Category, Comments, User


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['message', 'created', 'user']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
