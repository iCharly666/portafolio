from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about),
    #path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('register/', views.register, name='register'),  # Utiliza el nombre de función actualizado
    #path('login/', views.login_view, name='login'),  # Utiliza el nombre de función actualizado
    path('login/', views.login_view, name='login'),  # Utiliza el nombre de función actualizado
    path('logout/', views.logout_view, name='logout')

]
