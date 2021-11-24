from django.urls import path
from . import views

#directs to required location
urlpatterns = [
    path('register/', views.register, name='register-home'),
    path('login/', views.login, name='login-home'),
    path('update/', views.update, name='update-home'),
    path('login/update2/', views.update2, name='update2-home'),
    path('login/delete/', views.delete, name='delete-home'),
]
