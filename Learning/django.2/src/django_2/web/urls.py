from web.views import index
from django.urls import path,include

app_name="web"
urlpatterns = [
   path("",index,name="index")
]
