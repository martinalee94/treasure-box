# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.views import APIView

# class GoogleLogin(SocialLoginView):
#     # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
#     client_class = OAuth2Client


# class GoogleLogin(SocialLoginView):  # if you want to use Implicit Grant, use this
#     adapter_class = GoogleOAuth2Adapter
# class SelfGoogleLogin(APIView):
#     def post(self, request, format=None):
#         request.