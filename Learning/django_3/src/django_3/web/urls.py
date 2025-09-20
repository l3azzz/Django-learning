
from django.urls import path, include
from web.views import index , subscribe

app_name = "web"
urlpatterns = [
    path("",index,name="index"),
    path("subscribe", subscribe, name="subscribe")
]
