from django.urls import path
from .views import register, login_view, logout_view, home, add_post, user_count, all_posts

urlpatterns = [
    path('register/', register, name='register'),
    path('all/', all_posts, name='all-posts'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('add_post/', add_post, name='add_post'),
    path('user_count/', user_count, name='user_count'),
]
