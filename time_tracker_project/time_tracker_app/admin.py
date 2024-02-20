from django.contrib import admin
from .models import Project, TimeEntry, TaskDescription


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

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

