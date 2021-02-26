"""assessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from File_conversion import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path("",views.method,name='firstpage'),
    path('registration/',views.registration,name='reg_data'),

    path('login/',views.login,name='login'),
    path('loginvalidate/',views.authenticate,name='login_data'),

    path('fileconversion/',views.fileconversion,name='fileconversion'),

    path('logout/',views.logout,name='logout'),
    path('file_conver/',views.fconvert,name='file_convert')
]
