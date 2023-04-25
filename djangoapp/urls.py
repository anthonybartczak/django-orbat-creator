from .views import PlatoonsView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'api/platoons', PlatoonsView)

urlpatterns = [
    path('', include(router.urls)),
]