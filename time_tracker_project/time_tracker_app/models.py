from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AppUserManager(BaseUserManager):
    """Manager for custom user model."""

    def create_user(self, email, password=None):
        """Create and return a new user with an email and password."""
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        """Create and return a new superuser with an email and password."""
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class AppUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    user_id = models.AutoField(primary_key=True, default=334)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()

    # unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='app_users',
        related_query_name='app_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='app_users',
        related_query_name='app_user'
    )

    def __str__(self):
        return self.username


class Project(models.Model):
    """Project model."""
    user_id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TimeEntry(models.Model):
    """Time entry model."""

    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, db_column='user_id')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.project.name} - {self.date_time}"

    @property
    def week_number(self):
        return self.date_time.isocalendar()[1]

    @property
    def year(self):
        return self.date_time.year

    @property
    def week_start_date(self):
        week_start = self.date_time - timedelta(days=self.date_time.weekday())
        return week_start.date()

    @property
    def week_end_date(self):
        week_end = self.date_time + timedelta(days=(6 - self.date_time.weekday()))
        return week_end.date()

    @classmethod
    def get_weekly_summary(cls, user, year, week_number):
        start_date = datetime.strptime(f"{year}-{week_number}-1", "%Y-%W-%w").date()
        end_date = start_date + timedelta(days=6)
        entries = cls.objects.filter(user=user, date_time__range=[start_date, end_date])
        total_hours = sum(entry.hours for entry in entries)
        return total_hours

    @classmethod
    def get_project_totals(cls, user):
        projects = Project.objects.all()
        totals = {}
        for project in projects:
            entries = cls.objects.filter(user=user, project=project)
            total_hours = sum(entry.hours for entry in entries)
            totals[project.name] = total_hours
        return totals

    
class TaskDescription(models.Model):
    """Task description model."""

    time_entry = models.ForeignKey(TimeEntry, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.time_entry} - {self.description}"


# I decided not to work on this model lol 
""" Optional: WorkWeek model
class WorkWeek(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start_date = models.DateField()
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.week_start_date}" """
