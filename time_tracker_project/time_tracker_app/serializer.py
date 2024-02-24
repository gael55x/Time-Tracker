from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, TimeEntry, TaskDescription
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    class Meta:
        model = UserModel
        fields = '__all__'
        
    def create(self, clean_data):
        """Create a new user object."""
        user_obj = UserModel.objects.create_user(username=clean_data['username'], email=clean_data['email'], password=clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.save()
        return user_obj

class UserLoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def check_user(self, clean_data):
        """Check if the user exists."""
        user = authenticate(username=clean_data['username'], email=clean_data['email'], password=clean_data['password'])
        if not user:
            raise AssertionError('user not found')
        return user

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user details."""
    
    user_id = serializers.IntegerField(source='id')  # Map id to user_id
    
    class Meta:
        model = UserModel
        fields = ('user_id', 'email', 'username')

class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for project details."""
    
    class Meta:
        model = Project
        fields = ['id', 'user', 'name']

class TaskDescriptionSerializer(serializers.ModelSerializer):
    """Serializer for task description."""
    
    class Meta:
        model = TaskDescription
        fields = ['id', 'time_entry', 'description']

class TimeEntrySerializer(serializers.ModelSerializer):
    """Serializer for time entry details."""
    
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    week_number = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    week_start_date = serializers.SerializerMethodField()
    week_end_date = serializers.SerializerMethodField()

    class Meta:
        model = TimeEntry
        fields = ['id', 'user', 'project', 'hours', 'description', 'date_time', 'week_number', 'year', 'week_start_date', 'week_end_date']

    def get_week_number(self, obj):
        """Get the week number for the time entry."""
        return obj.week_number

    def get_year(self, obj):
        """Get the year for the time entry."""
        return obj.year

    def get_week_start_date(self, obj):
        """Get the start date of the week for the time entry."""
        return obj.week_start_date

    def get_week_end_date(self, obj):
        """Get the end date of the week for the time entry."""
        return obj.week_end_date
