from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/demo-request/', views.demo_request_api, name='demo_request_api'),
    path('product/<int:pk>/', views.product, name='product'),
]
