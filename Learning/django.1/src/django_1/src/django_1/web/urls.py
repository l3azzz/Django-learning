from django.urls import path
from web.views import index
from web.views import about


urlpatterns = [
    path("", index),
    path("about", about)
]
