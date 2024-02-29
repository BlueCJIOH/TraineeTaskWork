from rest_framework.routers import SimpleRouter

from creator.api.v1.views.creator import CreatorViewSet

router = SimpleRouter()
router.register(r"creator", CreatorViewSet, basename="creator")
urlpatterns = router.urls
