from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/',views.my_login,name='my_login'),
    path('logout/',views.my_logout,name='my_logout'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('profile/', views.profile_view, name='profile_view'),
]
