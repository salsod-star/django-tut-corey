from django.urls import path
from .views import (
    DisplayBlogListView,
    DisplayBlogDetailView,
    DisplayBlogCreateView,
    DisplayBlogUpdateView,
    DisplayBlogDeleteView
)
from . import views

urlpatterns = [
    path('', DisplayBlogListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', DisplayBlogDetailView.as_view(template_name='blog/post_detail.html'), name='blog-detail'),
    path('post/new/', DisplayBlogCreateView.as_view(template_name='blog/post_form.html'), name='blog-create'),
    path('post/<int:pk>/update/', DisplayBlogUpdateView.as_view(template_name='blog/post_form.html'),
         name='blog-update'),
    path('post/<int:pk>/delete/', DisplayBlogDeleteView.as_view(template_name='blog/post_confirm_delete.html'),
         name='blog-delete'),
    path('about/', views.about, name='blog-about')
]
