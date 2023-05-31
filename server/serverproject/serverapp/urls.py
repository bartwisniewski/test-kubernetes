from django.urls import path
from serverapp import views

urlpatterns = [
    path("", views.ServerApiView.as_view(), name="server-api"),
    path("live", views.LiveApiView.as_view(), name="server-api-live"),
]
