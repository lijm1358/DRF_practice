from django.urls import path

from .views import CheckinViewSet

urlpatterns = [
    path('', CheckinViewSet),
]
