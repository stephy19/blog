from django.urls import path
from blogapp.views import *

app_name = 'blogapp'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('category/<slug:category>/', post_list, name='category_post_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('/post_search/', post_search, name='post_search'),
    path('add/add/', add_post, name='add_post'),
    path('<slug:slug>/update/', post_update, name='post_update'),
    path('<slug:slug>/deleted/', post_delete, name='post_delete'),
    path('<int:post_id>/stream/', stream_view, name='stream_view'),
]
