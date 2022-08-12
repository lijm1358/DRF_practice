"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest.views import CheckinViewSet 
from recommend.views import recommend_list

router = routers.DefaultRouter()
router.register('Mapgo/checkin', CheckinViewSet)
#router.register('Mapgo/recommend', recommend_list)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mapgo/recommend', include('recommend.urls')),
    path('', include(router.urls)),
]
