from .views import PlatoonsView
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'api/platoons', PlatoonsView)