from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path("register/", views.register ,name="register"),
    path('car/<str:pk>/', views.car, name='car'),
    path('new-order/', views.new_order, name='new_order'),
    path('edit-order/<str:pk>', views.edit_car, name='edit_car'),
    path('chat/', views.new_order, name='new_order'),
    path('profile/', views.my_profile, name='my_profile'),
    path('user_profile/<str:pk>', views.user_profile, name='user_profile'),
    path('chat/<int:recipient_id>/', views.chat, name='chat'),
    path('my_chats/', views.view_chats, name='my_chats'),
    path('my_listings/', views.my_listings, name='my_listings'),
]
