from django.urls import include, path

from .views import GoogleLoginView

urlpatterns = [
    path("google/", GoogleLoginView.as_view(), name="google-login"),
]
