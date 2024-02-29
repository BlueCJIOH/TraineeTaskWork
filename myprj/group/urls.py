from rest_framework.routers import SimpleRouter

from group.api.v1.views.group import GroupViewSet

router = SimpleRouter()
router.register(r"group", GroupViewSet, basename="group")
urlpatterns = router.urls
