from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/',dashboard_view, name='dashboard'),
    path('profile/',edit_profile, name='edit_profile')
]