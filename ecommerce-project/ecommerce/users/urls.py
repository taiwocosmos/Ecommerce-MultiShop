from .import views as Userview
from django.urls import path
urlpatterns = [
    path('register/', Userview.Signup, name = 'signup'),
    path('profile/', Userview.profile, name = 'profile'),
]