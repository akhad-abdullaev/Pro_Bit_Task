from config.middleware import get_current_tenant_db
from rest_framework import serializers
from .models import TenantUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from tenants.models import TenantUser



class TenantUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUser
        fields = ['username', 'password', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return TenantUser.objects.db_manager(self.context['request'].tenant_db).create_user(**validated_data)



class TenantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUser
        fields = ['username', 'password', 'full_name']



class TenantLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        self.user = TenantUser.objects.using(get_current_tenant_db()).get(username=attrs['username'])
        return super().validate(attrs)
