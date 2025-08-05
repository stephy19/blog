from django.contrib import admin
from  .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','body', 'author', 'publish', 'statut','created', 'updated')
    list_filter = ('statut', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('author','created','publish')
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'body', 'created', 'updated')
    list_filter = ('username', 'email', 'body', 'created', 'updated')
    search_fields = ('username', 'email', 'body')
    ordering = ('username', 'email', 'body', 'created', 'updated')

    verbose_name = 'Comment'
    verbose_name_plural = 'Comments'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name', 'slug')
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'