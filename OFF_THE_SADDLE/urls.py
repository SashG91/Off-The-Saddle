from . import views
from django.urls import path

urlpatterns = [
    path("", views.ClimbList.as_view(), name="home"),
]
