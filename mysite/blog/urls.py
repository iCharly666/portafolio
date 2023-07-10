from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 

    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
    ]

    #path('about/', views.about),
    #path('', views.index),
    #path('hello/<str:username>', views.hello),
    #path('projects/', views.projects),
    #path('tasks/', views.tasks),
    #path('login/', views.login),
    #path('register/', views.register)
    #path('admin/', admin.site.urls),
    #path('', include('blog.urls')),