from django.urls import path
from. import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('privacy_policy', views.privacy_policy, name='privacy-policy'),
    path('post/<int:pk>/', views.post_details, name='post-detail'),
    path('post/new/', views.create_post, name='post-new'),
    path('post/<int:pk>/update', views.update_post, name='post-update'),
    path('post/<int:pk>/delete', views.delete_post, name='post-delete'),
    path('post/<str:username>', views.user_post_list, name='user-posts'),
    path('post/<int:pk>/thumbs_up/', views.post_thumbs_up, name='thumbs-up'),
    path('post/<int:pk>/remove_thumbs_up/', views.remove_post_thumbs_up, name='remove-thumbs-up'),
    path('post/recent/', views.recent_post, name='recent-post'),
    path('users/', views.user_list, name='user-list'),
]