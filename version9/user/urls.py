from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Crearpublicacion

urlpatterns=[
			path('login/', auth_views.LoginView.as_view(), {'template_name':"login.html"}, name='login'),
			path('logout/', auth_views.logout_then_login,  name='logout'),
			path('sigin/', Crearpublicacion.as_view(), name="no mames" )
]