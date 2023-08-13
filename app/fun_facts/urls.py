from fun_facts.views import FunDatesViewSet, PopularViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"dates", FunDatesViewSet, basename="dates")
router.register(r"popular", PopularViewSet, basename="popular")
urlpatterns = router.urls
