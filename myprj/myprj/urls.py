from django.contrib import admin
from django.urls import path, include
from core.swagger import urlpatterns as doc_urls

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += doc_urls
