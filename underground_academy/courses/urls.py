"""
URL configuration for underground_company project.

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
from django.urls import path , include
from courses.views import homepage , coursePage  ,LoginView , SignupView ,signout , checkout ,verifyPayment ,MyCoursesList
from django.conf.urls.static import static
from django.conf import settings
from underground_academy.settings import MEDIA_ROOT,MEDIA_URL

app_name = 'courses'
urlpatterns = [
    path("",homepage.home , name='home'),
     path("logout",signout, name='logout'),
    path('signup/', SignupView.as_view() , name = 'signup'),
    path('login/', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', checkout , name = 'check-out'),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
