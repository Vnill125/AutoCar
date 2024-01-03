from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path("register/", views.register ,name="register"),
    path('car/<str:pk>/', views.car, name='car'),
    path('new-order/', views.new_order, name='new_order'),
    path('chat/', views.new_order, name='new_order')
]
