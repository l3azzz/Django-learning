from django.urls import path
from web.views import index
from web.views import about

app_name = "web"

urlpatterns = [
    path("", index,name="index"),
    path("about", about,name="about")
]
