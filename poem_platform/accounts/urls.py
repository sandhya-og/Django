from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html',  next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create_poem/', views.create_poem, name='create_poem'),
    path('poem/<int:pk>/edit/', views.edit_poem, name='edit_poem'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('poem/<int:pk>/like/', views.like_poem, name='like_poem'),
    path('poem/<int:pk>/add_comment/', views.add_comment, name='add_comment'),  
    path('poem_search/', views.poem_search, name='poem_search'), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
