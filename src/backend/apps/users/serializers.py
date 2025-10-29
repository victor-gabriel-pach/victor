from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Team, TeamMember


class UserSerializer(serializers.ModelSerializer):
    """Serializer para visualização de usuário"""
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'nickname', 'email', 'user_type',
            'avatar', 'bio', 'coins', 'school', 'created_at'
        ]
        read_only_fields = ['id', 'coins', 'created_at']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer para registro de novos usuários"""
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'username', 'nickname', 'email', 'password', 'password2',
            'user_type', 'school'
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer para membros da equipe"""
    participant = UserSerializer(read_only=True)
    
    class Meta:
        model = TeamMember
        fields = ['id', 'participant', 'joined_at']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer para equipes"""
    tutor = UserSerializer(read_only=True)
    members = TeamMemberSerializer(many=True, read_only=True)
    members_count = serializers.IntegerField(read_only=True)
    is_complete = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Team
        fields = [
            'id', 'name', 'tutor', 'members', 'members_count',
            'is_complete', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TeamCreateSerializer(serializers.ModelSerializer):
    """Serializer para criação de equipes"""
    
    class Meta:
        model = Team
        fields = ['name', 'tutor']
