from xml.dom import ValidationErr

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import serializers

from .utils import Util

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["name", "email", "password", "password2"]
        extra_kwargs = {"password2": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "password and confirm passworrd doesnt match"
            )
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]


class UserPasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get("user")
        if password != password2:
            raise serializers.ValidationError(
                "password and conformation password does not match"
            )

        user.set_password("password")
        user.save()
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email"]

    def validate(self, attrs):
        email = attrs.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("encoded UID:", uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("password reset token:", token)
            link = "http://localhost:3000/api/user/reset/" + uid + "/" + token
            print("password reset link:", link)
            # send emal
            body = "click following link to reset your password" + link
            data = {"subject": "reset.password", "body": body, "to_email": user.email}
            Util.send_email(data)

            return attrs
        else:
            raise ValidationErr("you are not a registered error")


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["password", "password2"]

    def validate(self, attrs):
        try:
            password = attrs.get("password")
            password2 = attrs.get("password2")
            id = self.context.get("uid")
            token = self.context.get("token")
            print(id)
            if password != password2:
                raise serializers.ValidationError(
                    "password and conformation password does not match"
                )
            id = smart_str(urlsafe_base64_decode(id))
            user = User.objects.get(id=id)
            if not user:
                raise ValidationErr("User with specified ID does not exist")
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationErr("Token is not valid or expaired")
            user.set_password("password")
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationErr("token is not valid or expaired")
