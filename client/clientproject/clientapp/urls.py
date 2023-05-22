from django.urls import path
from clientapp import views

urlpatterns = [
    path("", views.ClientFormView.as_view(), name="client-form"),
    path(
        "<int:result>",
        views.ClientResultView.as_view(),
        name="client-result",
    ),
]
