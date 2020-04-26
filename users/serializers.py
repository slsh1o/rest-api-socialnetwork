from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                    'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, label='Confirm password', style={
                                    'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        password_confirm = validated_data['password_confirm']
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'user': 'This email address already in use'})
        if password != password_confirm:
            raise serializers.ValidationError(
                {'password': 'Passwords do not match!'})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user


class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Override `TokenObtainPairSerializer` to add `user_logged_in` signal
    to track when user login with jwt token.
    """
    def validate(self, attrs):
        data = super().validate(attrs)

        user_logged_in.send(sender=self.user.__class__, request=self.context['request'], user=self.user)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
