from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'common'

urlpatterns = [
    # default 템플릿 디렉토리는 registration/login.html
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    
]
