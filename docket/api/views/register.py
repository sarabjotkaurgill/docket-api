from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from docket.api.serializers.accounts import UserSerializer


# Register API
class RegisterUser(APIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json["token"] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
