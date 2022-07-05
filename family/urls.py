from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_req/', views.loginReq, name='login_req'),
    path('user_profile/', views.userProfile, name='user_profile'),
    path('add_member/', views.addMember, name='add_member'),
    path('update_head/', views.updateHead, name='update_head'),
    path('update_family_member/<int:pk>/', views.updateFamilyMember, name='update_family_member'),
    path('delete_family_member/<int:pk>/', views.deleteFamilyMember, name='delete_family_member'),
    path('view_profile/<int:pk>/', views.viewProfile, name='view_profile'),
]