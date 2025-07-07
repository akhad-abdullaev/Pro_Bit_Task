from main.apps.core.utils import create_tenant_database
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import authentication
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from .serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserDetailSerializer,
    UserUpdateSerializer
)
from .models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Organization
from .serializers import OrganizationCreateSerializer



class AuthUserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
        status_code = status.HTTP_201_CREATED 
        response = {
            'success': True,
            'statusCode': status_code,
            'message': 'User succesfully registered',
            'user': serializer.data
        }
        return Response(response, status=status_code)
    
user_registration_api_view = AuthUserRegistrationView.as_view()


class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response({'success': False, 'error': str(e)})

user_login_api_view = UserLoginView.as_view()


class UserRetrieveAPIView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = [authentication.JWTAuthentication]

    lookup_field = "guid"

user_retrieve_delete_api_view = UserRetrieveAPIView.as_view()


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = [authentication.JWTAuthentication]
    lookup_field = "guid"
    partial = True

user_update_api_view = UserUpdateAPIView.as_view()



class OrganizationCreateAPIView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        org = serializer.save(owner=self.request.user)
        create_tenant_database(org.db_name)

organization_create_api_view = OrganizationCreateAPIView.as_view()
