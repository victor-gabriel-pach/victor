from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Team, TeamMember


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'nickname', 'email', 'user_type', 'coins', 'created_at']
    list_filter = ['user_type', 'is_staff', 'is_active']
    search_fields = ['username', 'nickname', 'email']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('user_type', 'nickname', 'avatar', 'bio', 'coins', 'school')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ('user_type', 'nickname', 'email')
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'tutor', 'members_count', 'created_at']
    search_fields = ['name', 'tutor__nickname']
    list_filter = ['created_at']
    
    def members_count(self, obj):
        return obj.members_count
    members_count.short_description = 'Membros'


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['participant', 'team', 'joined_at']
    search_fields = ['participant__nickname', 'team__name']
    list_filter = ['joined_at']
