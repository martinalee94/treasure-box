from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
