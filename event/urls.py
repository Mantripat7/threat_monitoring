from rest_framework.routers import DefaultRouter
from event.views import EventViewSet, AlertViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="events")
router.register(r"alerts", AlertViewSet, basename="alerts")

urlpatterns = router.urls 
