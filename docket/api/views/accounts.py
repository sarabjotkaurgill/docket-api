from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

# serializers
from docket.api.serializers.accounts import AuthTokenSerializer


from rest_framework_simplejwt.views import TokenObtainPairView


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenSerializer