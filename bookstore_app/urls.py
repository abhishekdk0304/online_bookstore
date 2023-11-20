from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookstoreViewSet

router = DefaultRouter()

router.register('api',BookstoreViewSet)

urlpatterns = [
    path('',include(router.urls))
]
