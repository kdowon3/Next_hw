"""
URL configuration for BlogProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from BlogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.new, name='new'),
    path('', views.list, name='list'),
    path('detail/<int:post_pk>/', views.detail, name='detail'),
    path('category/<str:category>/', views.category_board, name='category_board'),
    path('delet-comment/<int:post_pk>/<int:comment_pk>',views.delete_comment, name='delete-comment'),
    path('add-reply/<int:post_pk>/<int:comment_pk>/', views.add_reply, name='add_reply'),
    path('delete-reply/<int:reply_pk>/', views.delete_reply, name='delete-reply'),
    path('base', views.base, name='base'),
]
