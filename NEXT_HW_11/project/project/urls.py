from django.contrib import admin
from django.urls import path, include
from app import views
from Authapp.views import login, signup, logout_user

urlpatterns = [
   path('', views.home, name='home'),
   path('new/', views.new, name='new'),
   path('detail/<int:post_pk>', views.detail, name='detail'),
   path('edit/<int:post_pk>', views.edit, name='edit'),
   path('delete/<int:post_pk>', views.delete, name='delete'),
   path('delete-comment/<int:post_pk>/<int:comment_pk>',views.delete_comment, name='delete-comment'),
   path('base/', views.base, name='base'),
   path("login", login, name="login"),
   path("signup", signup, name="signup"),
   path("logout", logout_user, name="logout"),
   path("admin/", admin.site.urls),
   path('accounts/', include('allauth.urls')),
]
