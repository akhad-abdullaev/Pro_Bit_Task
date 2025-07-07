import ast
from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Organization
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()



class UserRegistrationSerializer(serializers.ModelSerializer): 
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Enter confirm password',
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            "username",
            'password',
            'confirm_password',
        )    

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('confirm_password'):
            raise serializers.ValidationError({"message":"Password and confirm password don't match"}) 
        validated_data.pop('confirm_password') 
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class UserUpdateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = (
            "username",
            'user_permissions'
        ) 


class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['id'] = self.user.id
        data['guid'] = self.user.guid
        data['username'] = self.user.username        
        return data

    
   
class UserDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "guid",
            "username",
            "is_active",
            'created_at',
            'permissions'
        )

    def get_permissions(self, obj):
        permissions_data = obj.permissions
        if permissions_data is not None:
            return ast.literal_eval(permissions_data)
        else:
            return None


class UserUpdateSerializer(serializers.ModelSerializer):
    permissions = serializers.ListField(child=serializers.CharField())
    password = serializers.CharField(write_only=True, required=False) 
    class Meta:
        model = User
        fields = (
            "username",
            "is_active",
            "password",
            'permissions'
        )

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  
        if password is not None:
            instance.set_password(password)
        return super().update(instance, validated_data)
    


class OrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'db_name']
        read_only_fields = ['db_name']

    def validate(self, attrs):
        user = self.context['request'].user
        if hasattr(user, 'organization'):
            raise serializers.ValidationError("User already owns an organization.")
        return attrs

    def create(self, validated_data):
        # Auto-generate a safe db_name
        db_name = f"org_{uuid.uuid4().hex[:8]}"
        validated_data['db_name'] = db_name
        validated_data['owner'] = self.context['request'].user
        return Organization.objects.create(**validated_data)




    
        