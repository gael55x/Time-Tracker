from django.contrib import admin
from .models import Project, TimeEntry, TaskDescription, AppUser

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Custom admin for Project model."""
    list_display = ('get_username', 'name')
    fields = ('user', 'name')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('user')

    def get_username(self, obj):
        return obj.user.username if obj.user else None
    get_username.short_description = 'User'

@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'hours', 'description', 'date_time')
    list_filter = ('user', 'project', 'date_time')
    search_fields = ('user__username', 'project__name', 'description')

@admin.register(TaskDescription)
class TaskDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_entry', 'description')
    list_filter = ('time_entry',)
    search_fields = ('time_entry__user__username', 'time_entry__project__name', 'description')

admin.site.register(AppUser)
