from . import views
from django.urls import path

urlpatterns = [
    path('', views.ClimbList.as_view(), name='home'),
    path('<slug:slug>/', views.ClimbDetail.as_view(), name='climb_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/<int:pk>/delete_comment/',
         views.CommentDelete.as_view(), name="delete_comment"),
    path('403', views.Page403.as_view(), name='403'),
    path('404', views.Page404.as_view(), name='404'),
    path('500', views.Page500.as_view(), name='500'),
]
