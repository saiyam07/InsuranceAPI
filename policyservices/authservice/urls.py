'''
URL patterns of authentication services
'''
from knox import views as know_views
from django.urls import path
from .views import Login,UserView

urlpatterns = [
    path('user/login',Login.as_view()),
    path('user/get',UserView.as_view()),
    path('user/logout',know_views.LogoutView.as_view(),name="Logout View"),
]
