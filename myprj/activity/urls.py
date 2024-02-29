from rest_framework.routers import SimpleRouter

from activity.api.v1.views.activity import ActivityViewSet

router = SimpleRouter()
router.register(r"activity", ActivityViewSet, basename="activity")
urlpatterns = router.urls
