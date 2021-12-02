from django.urls import path
from . import views

#directs to required location
urlpatterns = [
    path('listapi/', views.ListView.as_view()),
    path('listdetail/<int:ssn>',views.ListIndividualView.as_view()),
    path('listapi/<int:ssn>',views.ListView.as_view()),
    path('register/', views.register, name='register-home'),
    path('login/', views.login, name='login-home'),
    path('list/', views.list, name='list-home'),
    path('login/update/', views.update, name='update-home'),
    path('login/delete/', views.delete, name='delete-home'),
]
