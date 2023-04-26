from .views import PlatoonsView, PlatoonsIdentifiersView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'api/platoons', PlatoonsView)
router.register(r'api/slugs/platoons', PlatoonsIdentifiersView)

urlpatterns = [
    path('', include(router.urls)),
]