from django.contrib import admin
from django.urls import path, include
from core.swagger import urlpatterns as doc_urls

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("creator.urls")),
    path("", include("product.urls")),
    path("", include("activity.urls")),
    path("", include("group.urls")),
]

urlpatterns += doc_urls
