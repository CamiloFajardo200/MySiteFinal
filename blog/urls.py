from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    like_view, AddCommentView, CommentDeleteView, CommentUpdateView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('example/', views.index, name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/comment/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('like/<int:pk>', like_view, name='like-post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='post-comment'),
]
