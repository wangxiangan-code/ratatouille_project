from django.contrib import admin
from django.urls import path
from mywebsite import views
from userauth.views import register_view
from userauth.views import login_view
from userauth.views import logout_view

urlpatterns = [
    path('', views.pageone_view, name='pageone'),  
    path('pageone/', views.pageone_view, name='pageone'),  
    path('pagetwo/', views.pagetwo_view, name='pagetwo'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
]
