# drf
from rest_framework import serializers
from django.contrib.auth.models import User

# simplet JWT
from rest_framework_simplejwt.serializers import TokenObtainSerializer, User
from rest_framework_simplejwt.tokens import RefreshToken


class AuthTokenSerializer(TokenObtainSerializer):
    username_field = User.EMAIL_FIELD

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        serializer = UserSerializer(self.user)
        data["user"] = serializer.data
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password","username", "is_superuser")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(email = validated_data['email'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'], username=validated_data['username'])
        return user
        fields = ("email", "first_name", "last_name", "password", "is_superuser")
        extra_kwargs = {"password": {"write_only": True}}
