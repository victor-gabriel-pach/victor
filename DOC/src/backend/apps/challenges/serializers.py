from rest_framework import serializers
from .models import Challenge, ChallengeCopy, Submission


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = [
            'id', 'title', 'description', 'instructions',
            'notebook_template', 'dataset_file', 'status',
            'metric_type', 'coins_reward', 'created_at',
            'published_at'
        ]
        read_only_fields = ['id', 'created_at', 'published_at']


class ChallengeCopySerializer(serializers.ModelSerializer):
    challenge_title = serializers.CharField(source='challenge.title', read_only=True)
    participant_nickname = serializers.CharField(source='participant.nickname', read_only=True)
    
    class Meta:
        model = ChallengeCopy
        fields = [
            'id', 'challenge', 'challenge_title', 'participant',
            'participant_nickname', 'copy_number', 'notebook_file',
            'is_submitted', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'copy_number', 'is_submitted', 'created_at', 'updated_at']


class SubmissionSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)
    challenge_title = serializers.CharField(source='challenge_copy.challenge.title', read_only=True)
    participant_nickname = serializers.CharField(source='challenge_copy.participant.nickname', read_only=True)
    
    class Meta:
        model = Submission
        fields = [
            'id', 'challenge_copy', 'team', 'team_name',
            'challenge_title', 'participant_nickname', 'accuracy',
            'execution_time', 'code_snapshot', 'submitted_at'
        ]
        read_only_fields = ['id', 'submitted_at']
