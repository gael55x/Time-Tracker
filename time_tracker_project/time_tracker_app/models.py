from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
