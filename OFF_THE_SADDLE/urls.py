from . import views
from django.urls import path

urlpatterns = [
    path("", views.ClimbList.as_view(), name="home"),
    path('<slug:slug>/', views.ClimbDetail.as_view(), name='climb_detail'),
]
