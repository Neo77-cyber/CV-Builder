from django.urls import path
from . import views
from .views import UserRegistrationView, UserAuthenticationView, ResumeCreateView


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('register', views.register, name= 'register'),
    path('signin/', views.signin, name = 'signin'),
    path('createresume/',  views.createresume, name = 'createresume'),
    path('cvtemplate/', views.cvtemplate, name= 'cvtemplate'),  
    path('logout', views.logout, name = 'logout'),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserAuthenticationView.as_view(), name='user-login'),
    path('api/createresume/', ResumeCreateView.as_view(), name = 'create-resume' ),
    path('api/downloadresume/', views.download_resume, name = 'download-resume' ),
]