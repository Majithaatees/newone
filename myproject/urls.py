"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('read',views.read,name='read'),
    path('view/<int:id>',views.view,name='view'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('userregister',views.userregister,name='userregister'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userhome',views.userhome,name='userhome'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('favourites/<int:id>',views.favourites,name='favourites'),
    path('viewfav',views.viewfav,name='viewfav'),

]
