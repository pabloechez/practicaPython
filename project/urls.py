"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import MyPostAPI, PostViewSet
from posts.views import HomeView, PostDetailView, PostFormView, BlogView, BlogDetailView
from users.api import UserViewSet
from users.views import LoginView, LogoutView, SignupView

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet, base_name='users')

urlpatterns = [
    path('admin/', admin.site.urls),

    # API URLs
    path('api/v1/', include(router.urls)),
    path('api/v1/blogs/', UserViewSet.as_view({'get': 'list'}), name='api-blogs'),
    path('api/v1/blogs/<int:id>/', MyPostAPI.as_view(), name='api-posts-mine'),

    path('', HomeView.as_view(), name='home'),
    path('blogs', BlogView.as_view(), name='blogs'),
    path('blogs/<username>', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<username>/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('blog/new-post', PostFormView.as_view(), name='post-create'),

    path('login', LoginView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
