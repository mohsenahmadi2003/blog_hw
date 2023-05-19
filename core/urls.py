from django.contrib import admin
from django.urls import path, include
handler404 = 'blog.views.handler404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
