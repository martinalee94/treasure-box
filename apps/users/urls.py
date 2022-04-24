from django.urls import include, path

from .views import GoogleLoginView, KakaoLoginView

urlpatterns = [
    path("google/", GoogleLoginView.as_view(), name="google-login"),
    path("kakao/", KakaoLoginView.as_view(), name="kakao-login"),
]
