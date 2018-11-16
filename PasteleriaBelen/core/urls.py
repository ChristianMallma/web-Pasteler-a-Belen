from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, StorePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('store/', StorePageView.as_view(), name="store"),
]