from .views import PlatoonsView, PlatoonsIdentifiersView, PlatoonsCreateView, LoadUserView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'create', PlatoonsCreateView, 'create')
#router.register(r'account/user', LoadUserView, 'account/user')
router.register(r'platoons', PlatoonsView, 'api/platoons')
router.register(r'slugs/platoons', PlatoonsIdentifiersView, 'api/slugs/platoons')

urlpatterns = [
    path(r'', include(router.urls)),
    path('user', LoadUserView.as_view()),
]