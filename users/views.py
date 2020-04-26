from rest_framework import response, decorators, status, permissions

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserRegistrationSerializer, AuthTokenObtainPairSerializer


class AuthTokenObtainPairView(TokenObtainPairView):
    """Override `TokenObtainPairView` to change `serializer_class` to our custom one."""
    serializer_class = AuthTokenObtainPairSerializer


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)
