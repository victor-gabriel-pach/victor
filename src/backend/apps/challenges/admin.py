from django.contrib import admin
from .models import Challenge, ChallengeCopy, Submission


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'metric_type', 'coins_reward', 'created_at', 'published_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ChallengeCopy)
class ChallengeCopyAdmin(admin.ModelAdmin):
    list_display = ['challenge', 'participant', 'copy_number', 'is_submitted', 'created_at']
    list_filter = ['is_submitted', 'created_at']
    search_fields = ['challenge__title', 'participant__nickname']


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['team', 'challenge_copy', 'accuracy', 'submitted_at']
    list_filter = ['submitted_at']
    search_fields = ['team__name', 'challenge_copy__challenge__title']
    readonly_fields = ['submitted_at']
