from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, TimeEntry, TaskDescription
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(
            username=attrs['email'],
            password=attrs['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid email or password.')
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']

class TaskDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDescription
        fields = ['id', 'time_entry', 'description']

class TimeEntrySerializer(serializers.ModelSerializer):
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
        return obj.week_number

    def get_year(self, obj):
        return obj.year

    def get_week_start_date(self, obj):
        return obj.week_start_date

    def get_week_end_date(self, obj):
        return obj.week_end_date
