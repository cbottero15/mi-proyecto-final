from django.urls import path
from blog.views import (DeletePost, ListPost, CreatePost, DetailPost, UpdatePost, DeletePost, SearchPostByName, inicio)

urlpatterns = [
    path('', inicio, name="inicio"),
    path('list/', ListPost.as_view(), name="list-post"),
    path('create/', CreatePost.as_view(), name="create-post"),
    path('detail/<int:pk>/', DetailPost.as_view(), name="detail-post"),
    path('update/<int:pk>/', UpdatePost.as_view(), name="update-post"),
    path('delete/<int:pk>', DeletePost.as_view(), name="delete-post"),
    path('search-by-name/', SearchPostByName.as_view(), name="search-by-name-post"),
]