from rest_framework import generics, permissions
from .models import TenantUser
from .serializer import TenantUserRegistrationSerializer, TenantUserSerializer
from config.middleware import get_current_tenant_db
from rest_framework.response import Response
from django.db import connections
from rest_framework_simplejwt.views import TokenObtainPairView



class TenantRegisterAPIView(generics.CreateAPIView):
    serializer_class = TenantUserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        tenant_db = get_current_tenant_db()
        if not tenant_db:
            return Response({"error": "X-TENANT header missing"}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(using=tenant_db)  
        return Response(serializer.data, status=201)

tenant_registration_api_view = TenantRegisterAPIView.as_view()



class TenantUserMeAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = TenantUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TenantUser.objects.using(get_current_tenant_db()).all()

    def get_object(self):
        return self.get_queryset().get(id=self.request.user.id)

tenant_user_me_api_view = TenantUserMeAPIView.as_view()



class TenantLoginAPIView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TenantUserSerializer

    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response({'success': False, 'error': str(e)})

tenant_login_api_view = TenantLoginAPIView.as_view()