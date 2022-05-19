from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.main, name='main'),
    path('login', views.login, name='login'),
    path('authUser', views.authUser, name='authUser'),
    path('monitor', views.monitor, name='monitor'),
    path('logout', views.logout, name='logout'),
    path('cambiarEstado', views.cambiarEstado, name='cambiarEstado'),
    path('moverPlaca', views.moverPlaca, name='moverPlaca')
]
