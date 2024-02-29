from rest_framework.routers import SimpleRouter
from product.api.v1.views.product import ProductViewSet

router = SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")
urlpatterns = router.urls
