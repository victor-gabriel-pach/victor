from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Team, TeamMember, ParticipantDocument
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    """Serializer para visualização de usuário"""
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'nickname', 'email', 'user_type',
            'avatar', 'bio', 'coins', 'school', 'school_grade', 'is_eligible', 'created_at'
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
            'user_type', 'school', 'school_grade'
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        # Determinar elegibilidade básica baseada na série/ano informado
        grade = validated_data.get('school_grade')
        if grade in ['9ef', '1em', '2em', '3em']:
            validated_data['is_eligible'] = True
        else:
            validated_data['is_eligible'] = False

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


class ParticipantDocumentSerializer(serializers.ModelSerializer):
    """Serializer para upload/visualização de documentos de participante"""
    user = UserSerializer(read_only=True)

    class Meta:
        model = ParticipantDocument
        fields = ['id', 'user', 'file', 'doc_type', 'status', 'uploaded_at', 'reviewed_at', 'review_notes']
        read_only_fields = ['id', 'user', 'status', 'uploaded_at', 'reviewed_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)
