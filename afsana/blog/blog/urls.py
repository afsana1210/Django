"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from blog_post.views import (
    blog_post_details_page,blog_post_create_view
)

from .views import ( home_page,
 new_example,
)
urlpatterns = [
    re_path(r'^homes?/$',home_page),
    # path('contact/',form_view),
    path('blog_create/',blog_post_create_view),
    # path('blog/',blog_post_details_page),
    path('new/',new_example),
    path('admin/', admin.site.urls),
]
